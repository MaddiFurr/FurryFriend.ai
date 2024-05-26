import discord
from discord import Webhook
from .BotService import bot
from .SettingsService import settings
from.LoggingService import log

# This function checks if the user has the proper permissions to run a command and returns true if they do, false if they don't
async def permission_checker(sender: discord.Member, level: str):
    mod_role_id = settings.MOD  # Get the mod role ID from settings
    admin_role_id = settings.ADMIN  # Get the admin role ID from settings

    user_role_ids = [role.id for role in sender.roles]  # Get the IDs of the roles the user has
    
    if level == 'mod' and mod_role_id in user_role_ids or admin_role_id in user_role_ids:
        return True
    elif level == 'admin' and admin_role_id in user_role_ids:
        return True
    else:
        return False
    