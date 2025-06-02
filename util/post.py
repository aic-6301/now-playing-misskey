from misskey import Misskey
import requests
import discord

def post(host, activity:discord.Spotify):
    """
    Posts the Spotify activity to a Misskey instance.

    Args:
        host (str): The host URL of the Misskey instance.
        activity (discord.Spotify): The Spotify activity to post.

    Returns:
        None
    """
    data = {"i":i,"url": activity.album_cover_url}
    response = requests.post(f"https://{host}/api/drive/files/upload-from-url", data=data)
    mi = Misskey(host=host, i=i)
    text = f"#nowplaying\nTrack:[{activity.title}]({activity.track_url})\nAlbum:{activity.album}\nArtist:{activity.artist}"
    mi.notes_create(text=text)