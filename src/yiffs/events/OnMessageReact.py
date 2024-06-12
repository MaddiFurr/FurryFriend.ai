import discord
from ...services.BotService import bot
from ...services.LoggingService import log
from ...services.DBService import check_react_role
import os

@bot.event
async def on_raw_reaction_add(payload):
    user = bot.get_user(payload.user_id)
    if user.bot:
        return
    channel = bot.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    guild = message.guild
    react_role = await check_react_role(guild.id, message.id, str(payload.emoji))
    if react_role is not None:
        role = discord.utils.get(guild.roles, id=react_role['role_id'])
        if role is not None:
            member = guild.get_member(user.id)  # Get the Member object for the user
            if member is not None:
                try:
                    await member.add_roles(role)  # Use the Member object here
                    await log(None, f"Added role {role.name} to {member.name} (Reaction Role)", None, None, channel)
                except discord.Forbidden:
                    print(f"Missing permissions to add role {role.name} to {member.name} (Reaction Role)")
            else:
                print("Member not found")
        else:
            print("Role not found")

@bot.event
async def on_raw_reaction_remove(payload):
    user = bot.get_user(payload.user_id)
    if user.bot:
        return
    channel = bot.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    guild = message.guild
    react_role = await check_react_role(guild.id, message.id, str(payload.emoji))
    if react_role is not None:
        role = discord.utils.get(guild.roles, id=react_role['role_id'])  # Use `guild.roles` here
        if role is not None:
            member = guild.get_member(user.id)  # Get the Member object for the user
            if member is not None:
                await member.remove_roles(role)
                await log(None, f"Removed role {role.name} from {member.name} (Reaction Role)", None, None, channel)  # Use `channel` here

@bot.event
async def on_raw_reaction_clear_emoji(payload):
    guild = bot.get_guild(payload.guild_id)
    if guild is None:
        return
    react_role = await check_react_role(guild.id, payload.message_id, str(payload.emoji))
    if react_role is not None:
        role = discord.utils.get(guild.roles, id=react_role['role_id'])
        if role is not None:
            for member in guild.members:
                if role in member.roles:
                    await member.remove_roles(role)
                    channel = bot.get_channel(payload.channel_id)
                    log(None, f"Removed role {role.name} from {member.name} (Reaction Role)", None, None, channel)