import os
import discord
import nextcord
from nextcord import Interaction, SlashOption
from nextcord.ext import commands
from dotenv import load_dotenv
load_dotenv()

log_channel_id = 1005112957530804335

description = """An example bot to showcase the nextcord.ext.commands extension
module.
There are a number of utility commands being showcased here."""

intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True
intents.presences = True

activity = discord.Activity(type=discord.ActivityType.listening, name="to nature")

bot = commands.Bot(command_prefix=".", status=discord.Status.online, activity=activity, description=description, intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")


@bot.event
async def on_raw_message_delete(message):
    embed = nextcord.Embed(
        title="{}'s messae deleted.".format(message.author.name),
        description=message.content
    )
    channel = bot.get_channel(log_channel_id)
    await channel.send(embed=embed)
    print(message)


@bot.slash_command(description="Information about the user!")
async def joined(ctx, member: nextcord.Member):
    """Says when a member joined."""
    await ctx.send(f"{member.name} joined in {member.joined_at}")


@bot.command()
async def joined(ctx, member: nextcord.Member):
    """Says when a member joined."""
    await ctx.send(f"{member.name} joined in {member.joined_at}")


@bot.slash_command(description="Replies with pong!")
async def ping(interaction: nextcord.Interaction):
    await interaction.send("Pong!", ephemeral=True)


@bot.command()
async def ping(interaction: nextcord.Interaction):
    await interaction.send("Pong!")


@bot.slash_command(description="Converts Celsius to Farenheit!")
async def ctof(
        interaction: Interaction,
        number: int = SlashOption(description="Your number", required=False),
):
    if not number:
        await interaction.response.send_message("No number was specified!", ephemeral=True)
    else:
        number = number * 9 / 5 + 32
        await interaction.response.send_message(f"You chose {number}!")


@bot.slash_command(description="Converts Farenheit to Celsius!")
async def ftoc(
        interaction: Interaction,
        number: int = SlashOption(description="Your number", required=False),
):
    if not number:
        await interaction.response.send_message("No number was specified!", ephemeral=True)
    else:
        number = (number- 32) * 5 / 9
        await interaction.response.send_message(f"You chose {number}!")


bot.run(os.getenv("BOT_TOKEN"))
