import discord
from discord import app_commands as apc
from ...services.BotService import bot
from ...services.PermissionChecker import permission_checker
from ...services.LoggingService import log
from ...services.DBService import add_all_users

async def dbupdate(interaction: discord.Interaction):
    """Validate a user's permissions and add all users in a guild to the database"""
    if await permission_checker(interaction.user, 'admin') == False:
        await interaction.response.send_message("You don't have permission to run this command!", ephemeral=True)
        await log(None, "{} ({}) tried to run the add_all_users command without permission.".format(interaction.user.name,interaction.user.id), "/settings add_all_users <NoPerms>", interaction.user, interaction.channel)
        return

    try:
        await add_all_users(interaction.guild)
        await interaction.response.send_message('All users have been added to the database.', ephemeral=True)
        await log(None, "{} ({}) has run the add_all_users command.".format(interaction.user.name,interaction.user.id), "/settings add_all_users", interaction.user, interaction.channel)
    except ValueError as e:
        await interaction.response.send_message(str(e), ephemeral=True)