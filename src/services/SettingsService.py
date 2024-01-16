import discord
from discord.ext import commands
import configparser

# Load bot configuration from bot.conf
config = configparser.ConfigParser()
config.read("./bot.conf")
TOKEN = config.get("Bot", "TOKEN")
GUILD = config.get("Bot", "GUILD")
MOD = config.get("Bot", "MOD")
ADMIN = config.get("Bot", "ADMIN")
STATUS = config.get("Bot", "STATUS")

class settings:
    def __init__(self, TOKEN, MOD, ADMIN, GUILD):
        self.TOKEN = TOKEN
        self.MOD = MOD
        self.ADMIN = ADMIN
        self.GUILD = GUILD
        self.STATUS = STATUS

settings = settings(TOKEN, MOD, ADMIN, GUILD, STATUS)