import discord
from discord.ext import commands
from discord import app_commands


class about(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name="about", description="Get information about the bot")
    async def about(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="再生してるやつMisskeyに送るやつ",
            description="""このボットは、Spotifyで再生中の曲をMisskeyに送信します。(今のところSpotifyのみ対応。そのうちMusic Presenceにも対応するかも。)
このBotはMisskeyとDiscordの連携を行うため、Tokenを保存していますが、作成者は、Tokenを使用したり、公開したりすることは必ず行いません。
ユーザーは、自分のTokenを削除したくなった場合、/unregisterコマンドを使用して、Botから情報を削除することができるものとします。""",
            color=discord.Color.blue()
        )
        embed.add_field(name="作者", value="[あいしぃー](https://me.aisii.net)", inline=True)

        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(about(bot))