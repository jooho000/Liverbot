import os
import discord
from discord.ext import commands
from rpg_game import handleRequest, handle_guild_request

# Load bot token
DISCORD_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Set up bot with intents
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot is online as {bot.user}")

@bot.command()
async def rpg(ctx, name: str, command: str, *args):
    """Handles RPG game commands"""
    message = f"rpg {name} {command} {' '.join(args)}"
    response = handleRequest(message)
    await ctx.send(response)

@bot.command()
async def guild(ctx, name: str, action: str, *args):
    """Handles Guild system commands"""
    message = f"guild {name} {action} {' '.join(args)}"
    response = handle_guild_request(message)
    await ctx.send(response)

bot.run(DISCORD_TOKEN)
