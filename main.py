import discord
from discord.ext import commands
import sqlite3
import dotenv
import os
import datetime
import traceback

dotenv.load_dotenv()
token = os.getenv('token')


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="aiu!",
            intents=discord.Intents.all(),
            
            )
        self.start_time = datetime.datetime.now()
        self.user_cache = {}
        
    async def on_ready(self):
        self.db = sqlite3.connect('data/data.db')
        self.db.execute(
            "CREATE TABLE IF NOT EXISTS users (user INTEGER PRIMARY KEY, address TEXT, token TEXT)"
        )
        self.db.commit()
        for file in os.listdir("./cogs"):
            if file.endswith('.py'):
                try:
                    await self.load_extension(f'cogs.{file[:-3]}')
                    print(f"Loaded cogs: cogs.{file[:-3]}")
                except Exception as e:
                    print(f"cogs.{file[:-3]} failed to load", e)
                    traceback.print_exc()
        try:
            await self.load_extension("jishaku") # Load jishaku
            print("Loaded extension: Jishaku")
        except Exception:
            traceback.print_exc()
        
        data = self.db.execute(
            "SELECT * FROM users"
        )
        for row in data:
            user_id, address, token = row
            self.user_cache[user_id] = {
                "address": address,
                "token": token
            }
        print(f"Loaded {len(self.user_cache)} users from the database.")
        sync = await self.tree.sync() # Slash command automatic sync
        await self.change_presence(activity=discord.CustomActivity(name="Misskey <=> Discord <=> Spotify"), status="Online")
        print(f"起動完了!\nLogging in {self.user.name} ({self.user.id})\n 同期済みコマンド：{len(sync)}")



if __name__ == "__main__":
    print("Program starting...")
    bot=MyBot()
    try:
        bot.run(token)
    except Exception:
        print("Program Crashed!\n")
        traceback.print_exc()