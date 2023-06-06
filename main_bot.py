import discord
from discord.ext import commands
import os
import configparser
import logging
import logging.handlers
import asyncio

# Load bot configuration from bot.conf
config = configparser.ConfigParser()
config.read("bot.conf")
TOKEN = config.get("Bot", "TOKEN")
PREFIX = config.get("Bot","PREFIX")

# Logger Settings
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')


# Define required intents and create the bot
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

async def load_cogs():
    for filename in os.listdir("./yiffs"):
        if filename.endswith(".py"):
            cog_name = filename[:-3]
            try:
                await bot.load_extension(f"yiffs.{cog_name}")
                print(f"Loaded cog: {cog_name}")
            except Exception as e:
                print(f"Failed to load cog {cog_name}: {str(e)}")

@bot.command()
async def reload_cogs(ctx):
    await load_cogs()
    await ctx.send("Reloaded cogs.")

async def main():
    await load_cogs()
    await bot.start(TOKEN)
    

asyncio.run(main())