import discord
from discord import app_commands as apc
from ...services.BotService import bot
from ...services.PermissionChecker import permission_checker
from ...services.LoggingService import log

async def hello(interaction: discord.Interaction):
        """Say "hello" to the bot!"""
        await interaction.response.send_message('Hello {}! Ya cutie!'.format(interaction.user.mention), ephemeral=True)
        await log(None, "{} ({}) has run the hello command.".format(interaction.user.name,interaction.user.id), "/info hello", interaction.user, interaction.channel)
        return