import discord
from discord.ext import commands
from pymongo import MongoClient
from .BotService import bot
from .SettingsService import settings
from datetime import datetime


async def get_db():
    """Get the database connection"""
    client = MongoClient(settings.MONGO_URI)
    db = client[settings.MONGO_DB]
    return db

async def add_new_user(user_id: int, name: str, nickname: str, account_creation_date: datetime, join_date: datetime):
    """Add a new user to the database when they join"""
    db = await get_db()
    collection = db['users']
    result = collection.insert_one({
        '_id': user_id,
        'name': name,
        'nickname': nickname,
        'account_creation_date': account_creation_date,
        'join_date': join_date,
    })
    return result

async def write_user_data(user_id: int, data: dict):
    """Write data for a specific user to the database"""
    db = await get_db()
    collection = db['users']
    result = collection.update_one({'_id': user_id}, {'$set': data}, upsert=True)
    return result

async def write_server_data(server_id: int, data: dict):
    """Write data for a specific server to the database"""
    db = await get_db()
    collection = db['servers']
    result = collection.update_one({'_id': server_id}, {'$set': data}, upsert=True)
    return result

async def increment_user_action(user_id: int, command_name: str):
    """Increment the usage count for a specific action for a specific user"""
    db = await get_db()
    collection = db['users']
    result = collection.update_one({'_id': user_id}, {'$inc': {f'action.{command_name}': 1}}, upsert=True)
    return result

async def update_username(user_id: int, name: str, nickname: str):
    """Update a user's name and nickname in the database"""
    db = await get_db()
    collection = db['users']
    result = collection.update_one({'_id': user_id}, {'$set': {'username': name, 'nickname': nickname}}, upsert=True)
    return result

async def increment_channel_action(channel_id: int, command_name: str):
    """Increment the usage count for a specific action for a specific channel"""
    db = await get_db()
    collection = db['channels']  # Use a 'channels' collection
    result = collection.update_one({'_id': channel_id, f'actions.{command_name}': {'$exists': True}}, {'$inc': {f'actions.{command_name}': 1}})
    if result.matched_count == 0:
        result = collection.update_one({'_id': channel_id}, {'$set': {f'actions.{command_name}': 1}}, upsert=True)
    return result

async def update_channel_name(channel_id: int, name: str):
    """Update a channel's name in the database"""
    db = await get_db()
    collection = db['channels']
    result = collection.update_one({'_id': channel_id}, {'$set': {'channel_name': name}}, upsert=True)
    return result

async def add_all_users(guild):
    db = await get_db()
    collection = db["users"]
    for member in guild.members:
        user_id = member.id
        username = member.name
        discriminator = member.discriminator
        avatar = str(member.avatar.url) if member.avatar else None
        bot = member.bot
        join_date = member.joined_at  # Get the join date
        creation_date = member.created_at  # Get the account creation date
        user = collection.find_one({"_id": user_id})
        if user is None:
            result = collection.insert_one({
                "_id": user_id,
                "username": username,
                "discriminator": discriminator,
                "avatar": avatar,
                "bot": bot,
                "join_date": join_date,
                "creation_date": creation_date
            })
        else:
            result = collection.update_one({"_id": user_id}, {"$set": {
                "username": username,
                "discriminator": discriminator,
                "avatar": avatar,
                "bot": bot,
                "join_date": join_date,
                "creation_date": creation_date
            }})