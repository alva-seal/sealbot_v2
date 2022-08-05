from nextcord.ext import commands
import nextcord
import os
from dotenv import load_dotenv
load_dotenv()



bot = commands.Bot()

@bot.slash_command(description="Replies with pong!")
async def ping(interaction: nextcord.Interaction):
    await interaction.send("Pong!", ephemeral=True)

bot.run(os.getenv("BOT_TOKEN"))