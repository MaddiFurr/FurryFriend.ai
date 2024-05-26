import discord
from discord import app_commands as apc
from ...services.BotService import bot
from ...services.PermissionChecker import permission_checker

#async def setjoinrole(interaction: discord.Interaction, newrole: discord.Role):
    #"""Set the role assigned to users upon joining"""
    #if await permission_checker(interaction.user, 'admin') == False:
    #    await interaction.response.send_message("You don't have permission to run this command!", ephemeral=True)
    #    return

    # Create a DatabaseService instance
    #db_service = DatabaseService(interaction.guild.id, bot.user.name.replace(' ', '_'))

    # Write the new role to the database
    #db_service.write_data('guild_settings', {'setting_name': 'new_member_role', 'setting_value': newrole.id})

    #await interaction.response.send_message(f'New member role set to:\n`{newrole.name}`', ephemeral=True)
    #print(f"Set Join Role command ran by {interaction.user.name} ({interaction.user.id}). Set role to: {newrole.name}")