import discord
from discord.ext import commands
import configparser
import os

# Get the absolute path of the directory of the current script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Construct the path to the bot.conf file
conf_path = os.path.join(dir_path, '../../bot.conf')

# Load bot configuration from bot.conf
config = configparser.ConfigParser()
config.read(conf_path)
TOKEN = config.get("Bot", "TOKEN")
GUILD = config.get("Bot", "GUILD")
MOD = config.get("Bot", "MOD")
ADMIN = config.get("Bot", "ADMIN")
STATUS = config.get("Bot", "STATUS")

class settings:
    def __init__(self, TOKEN, MOD, ADMIN, GUILD, STATUS):
        self.TOKEN = TOKEN
        self.MOD = MOD
        self.ADMIN = ADMIN
        self.GUILD = GUILD
        self.STATUS = STATUS

settings = settings(TOKEN, MOD, ADMIN, GUILD, STATUS)