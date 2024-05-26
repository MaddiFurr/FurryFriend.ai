import discord
from discord.ext import commands
from pymongo import MongoClient
from .BotService import bot
from .SettingsService import settings

def connect(guild_id=settings.GUILD, bot_name="furryfriendai"):
    username = settings.MONGO_USER
    password = settings.MONGO_PASS
    dbhost = settings.MONGO_HOST
    client = MongoClient(f'mongodb://{username}:{password}@{dbhost}/')
    db_name = f"{guild_id}_{bot_name}"
    db = client[db_name]
    return db

def fetch_data(collection_name, query={}, guild_id=settings.GUILD, bot_name="furryfriendai"):
    db = connect(guild_id, bot_name)
    collection = db[collection_name]
    data = collection.find(query)
    return list(data)

def write_data(collection_name, data, guild_id=settings.GUILD, bot_name="furryfriendai"):
    db = connect(guild_id, bot_name)
    collection = db[collection_name]
    result = collection.insert_one(data)
    return result.inserted_id