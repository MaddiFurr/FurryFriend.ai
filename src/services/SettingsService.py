import discord
from discord.ext import commands
import configparser
import os

# Get the absolute path of the directory of the current script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Construct the path to the bot.conf file
conf_path = os.path.join(dir_path, '../../configs/bot.conf')

# Load bot configuration from bot.conf
config = configparser.ConfigParser()
config.read(conf_path)
TOKEN = config.get("Bot", "TOKEN")
GUILD = config.get("Bot", "GUILD")
MOD = int(config.get("Bot", "MOD"))
ADMIN = int(config.get("Bot", "ADMIN"))
STATUS = config.get("Bot", "STATUS")
LOG_CHANNEL = config.get("Bot", "LOG_CHANNEL")
GOOGLE_API_KEY = config.get("Bot", "GOOGLE_API_KEY")
AUTO_ROLE = config.get("Bot", "AUTO_ROLE")

class settings:
    def __init__(self, TOKEN, MOD, ADMIN, GUILD, STATUS, LOG_CHANNEL, GOOGLE_API_KEY, AUTO_ROLE):
        self.TOKEN = TOKEN
        self.MOD = MOD
        self.ADMIN = ADMIN
        self.GUILD = GUILD
        self.STATUS = STATUS
        self.LOG_CHANNEL = LOG_CHANNEL
        self.GOOGLE_API_KEY = GOOGLE_API_KEY
        self.AUTO_ROLE = AUTO_ROLE

settings = settings(TOKEN, MOD, ADMIN, GUILD, STATUS, LOG_CHANNEL, GOOGLE_API_KEY, AUTO_ROLE)