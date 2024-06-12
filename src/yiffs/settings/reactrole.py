import discord
from discord import app_commands as apc
from ...services.BotService import bot
from ...services.PermissionChecker import permission_checker
from ...services.DBService import add_react_role, remove_react_role, check_react_role
from ...services.LoggingService import log

async def add_reaction(interaction: discord.Interaction, emoji: str, message_id: int, role_id: str):
    """Add a reaction to a message"""
    if not await permission_checker(interaction.user, "mod"):
        await interaction.response.send_message("You do not have permission to add a react roles", ephemeral=True)
        return
    role_id_str = role_id.strip("<@&>")
    role_id_int = int(role_id_str)
    result = await add_react_role(interaction.guild.id, message_id, emoji, role_id_int)

    # Fetch the message
    channel = bot.get_channel(interaction.channel.id)
    message = await channel.fetch_message(message_id)

    # Add the reaction to the message
    await message.add_reaction(emoji)

    await interaction.response.send_message(f"Added reaction {emoji} to message {message_id}.", ephemeral=True)
    await log(None, f"Added reaction {emoji} to message {message_id}.", None, None, interaction.channel)
    return result

async def remove_reaction(interaction: discord.Interaction, message_id: int, role_id: str):
    """Remove a reaction from a message and clear all reactions of the emoji"""
    if not await permission_checker(interaction.user, "admin"):
        await interaction.response.send_message("You do not have permission to remove a react roles", ephemeral=True)
        return
    
    react_role = await check_react_role(interaction.guild.id, message_id, role_id)
    if react_role is None:
        await interaction.response.send_message("No reaction role found for this message", ephemeral=True)
        return

    emoji = react_role['emoji']
    result = await remove_react_role(interaction.guild.id, message_id, emoji)

    # Fetch the message
    channel = bot.get_channel(interaction.channel.id)
    message = await channel.fetch_message(message_id)

    # Remove the reaction from the message
    await message.clear_reaction(emoji)

    await interaction.response.send_message(f"Removed reaction {emoji} from message {message_id}.", ephemeral=True)
    await log(None, f"Removed reaction {emoji} from message {message_id}.", None, None, interaction.channel)
    return result