import discord
from discord import Webhook
from .BotService import bot
from .SettingsService import settings

#This function checks if the user has the proper permissions to run a command and returns true if they do, false if they don't
async def permission_checker(sender: discord.Member, level: str):
    mod_role_name = settings.MOD  # Get the mod role name from settings
    admin_role_name = settings.ADMIN  # Get the admin role name from settings

    user_roles = [role.name for role in sender.roles]  # Get the names of the roles the user has
    
    if level == 'mod' and mod_role_name in user_roles or admin_role_name in user_roles:
        return True
    elif level == 'admin' and admin_role_name in user_roles:
        return True
    else:
        print("User {} ({}) attempted to run a command without proper permissions".format(sender.name,sender.id))
        return False
    