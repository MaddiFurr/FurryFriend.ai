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
CONSOLE_CHANNEL = config.get("Bot", "CONSOLE_CHANNEL")
GOOGLE_API_KEY = config.get("Bot", "GOOGLE_API_KEY")
AUTO_ROLE = config.get("Bot", "AUTO_ROLE")
MONGO_URI = config.get("Bot", "MONGO_URI")
MONGO_DB = config.get("Bot", "MONGO_DB")

class settings:
    def __init__(self, TOKEN, MOD, ADMIN, GUILD, STATUS, LOG_CHANNEL, GOOGLE_API_KEY, AUTO_ROLE, MONGO_URI, MONGO_DB,CONSOLE_CHANNEL):
        self.TOKEN = TOKEN
        self.MOD = MOD
        self.ADMIN = ADMIN
        self.GUILD = GUILD
        self.STATUS = STATUS
        self.LOG_CHANNEL = LOG_CHANNEL
        self.GOOGLE_API_KEY = GOOGLE_API_KEY
        self.AUTO_ROLE = AUTO_ROLE
        self.MONGO_URI = MONGO_URI
        self.MONGO_DB = MONGO_DB
        self.CONSOLE_CHANNEL = CONSOLE_CHANNEL

settings = settings(TOKEN, MOD, ADMIN, GUILD, STATUS, LOG_CHANNEL, GOOGLE_API_KEY, AUTO_ROLE, MONGO_URI, MONGO_DB, CONSOLE_CHANNEL)