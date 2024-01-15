import discord
from discord.ext import commands

## Create the bot
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.presences = True
intents.members = True
bot = commands.Bot(command_prefix=".",intents=intents)