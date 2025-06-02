import discord
from discord.ext import commands
from discord import app_commands

from misskey import MiAuth, Misskey
import re
import uuid

class register(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.auth_sessions = {}
    
    @app_commands.command(name="register", description="Botと連携します。")
    @app_commands.describe(instance="MisskeyのインスタンスURL (例: https://misskey.io)")
    async def register(self, interaction: discord.Interaction, instance: str):
        if interaction.user.id in self.bot.user_cache:
            await interaction.response.send_message("アカウントはすでに登録されています。", ephemeral=True)
            return
        server = re.sub(r"https?://", "", instance)
        session = uuid.uuid4()
        auth = MiAuth(address=server, session_id=session, name="Now Playing with Spotify",
                      permission=[
                        "read:account",
                        "write:notes",
                        "read:drive",
                        "write:drive",
                      ])
        url = auth.generate_url()
        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="完了", style=discord.ButtonStyle.green, custom_id="complete_auth"))
        await interaction.response.send_message(f"[このリンク]({url} )から認証を完了させてください。認証が完了したら、完了ボタンを押してください。", ephemeral=True, view=view)

        self.auth_sessions[interaction.user.id] = (session, instance, auth)
    
    @app_commands.command(name="unregister", description="Botとの連携を解除します。")
    async def unregister(self, interaction: discord.Interaction):
        if interaction.user.id in self.bot.user_cache:
            del self.bot.user_cache[interaction.user.id]
            self.bot.db.execute("DELETE FROM users WHERE user = ?", (interaction.user.id,))
            self.bot.db.commit()
            await interaction.response.send_message("アカウントの登録を解除しました。", ephemeral=True)
        else:
            await interaction.response.send_message("アカウントは登録されていません。", ephemeral=True)

    @commands.Cog.listener()
    async def on_interaction(self, interaction: discord.Interaction):
        if interaction.type == discord.InteractionType.component:
            await self.on_button_click(interaction)


    async def on_button_click(self, interaction: discord.Interaction):
        if interaction.data["custom_id"] == "complete_auth":
            session, instance, MiAuth = self.auth_sessions.get(interaction.user.id, (None, None, None))
            if session:
                print(f"Session: {session}, Instance: {instance}, User: {interaction.user.id}")
                auth = MiAuth
                
                token = auth.check()
                try:
                    if not token:
                        await interaction.response.send_message("認証に失敗しました。もう一度やり直してください。", ephemeral=True)
                        return
                    self.bot.db.execute(
                        "INSERT INTO users (user, address, token) VALUES (?, ?, ?) ON CONFLICT (user) DO UPDATE SET token = ?",
                        (interaction.user.id, instance, token, token)
                    )
                    self.bot.db.commit()
                    self.bot.user_cache[interaction.user.id] = {
                        "address": instance,
                        "token": token
                    }
                    await interaction.response.send_message(f"認証が完了しました！\nユーザー名: {Misskey(address=instance, i=token).i()['name']}@{instance}", ephemeral=True)
                except Exception as e:
                    print(f"Error during registration: {e}")
                    await interaction.response.send_message("認証中にエラーが発生しました。もう一度やり直してください。", ephemeral=True)
            else:
                await interaction.response.send_message("セッションが見つかりませんでした。もう一度やり直してください。", ephemeral=True)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(register(bot))