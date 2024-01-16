import discord
from discord import app_commands as apc
from ...services.BotService import bot
from ...services.PermissionChecker import permission_checker

async def hello(interaction: discord.Interaction):
        """Say "hello" to the bot!"""
        await interaction.response.send_message('Hello {}! Ya cutie!'.format(interaction.user.mention), ephemeral=True)
        print("Hello command ran by {} ({})".format(interaction.user.name,interaction.user.id))