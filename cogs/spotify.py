import discord
from discord.ext import commands
from discord import app_commands

import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import asyncio

from typed_spotipy import TypedSpotipy

from misskey import Misskey

class spotify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        cc_manager = SpotifyClientCredentials(
            client_id=os.getenv('SPOTIFY_CLIENT_ID'),
            client_secret=os.getenv('SPOTIFY_CLIENT_SECRET')
        )
        self.spotify_client = spotipy.Spotify(client_credentials_manager=cc_manager)
        self.before_activity = {}


    @commands.Cog.listener()
    async def on_presence_update(self, before, after):
        if after.bot:
            return
        
        if after.id not in self.bot.user_cache:
            return
        
        before_spotify = None
        if before.activities is not None:
            for activity in before.activities:
                if isinstance(activity, discord.Spotify):
                    before_spotify = activity
                    break
        
        current_spotify = None
        for activity in after.activities:
            if isinstance(activity, discord.Spotify):
                current_spotify = activity
                break
        
        user_id = after.id
        
        if current_spotify and (not before_spotify or before_spotify.title != current_spotify.title):
            current_track_key = f"{user_id}_{current_spotify.track_id}"
            if current_track_key not in self.before_activity:
                self.before_activity[current_track_key] = current_spotify.title
                
                await asyncio.sleep(5)
                
                current_spotify_after_wait = None
                for activity in after.activities:
                    if isinstance(activity, discord.Spotify):
                        current_spotify_after_wait = activity
                        break
                
                if current_spotify_after_wait and current_spotify_after_wait.track_id == current_spotify.track_id:
                    track = TypedSpotipy(self.spotify_client).track(current_spotify.track_id)
                    text = f"""#NowPlaying
Track : [{track.name}]({track.external_urls.spotify}) 
Album: [{track.album.name}]({track.album.external_urls.spotify}) 
Artist: {', '.join([f'[{artist.name}]({artist.external_urls.spotify})' for artist in track.artists])}"""
                    mk = Misskey(address=self.bot.user_cache[user_id]['address'], i=self.bot.user_cache[user_id]['token'])
                    mk.notes_create(
                        text=text,
                        visibility="home"
                    )
        
        elif not current_spotify and before_spotify:
            keys_to_remove = [key for key in self.before_activity.keys() if key.startswith(f"{user_id}_")]
            for key in keys_to_remove:
                del self.before_activity[key]
                
                
async def setup(bot: commands.Bot):
    await bot.add_cog(spotify(bot))