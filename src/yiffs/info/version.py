import discord
from discord import app_commands as apc
from ...services.BotService import bot
from ...services.PermissionChecker import permission_checker
from ...services.LoggingService import log


async def version(interaction: discord.Interaction):
        """Tells you what version of the bot software is running."""
        await interaction.response.send_message('Bot Running: DEV 0.0.1', ephemeral=True)
        await log(None, "{} ({}) has run the version command.".format(interaction.user.name,interaction.user.id), "/info version", interaction.user, interaction.channel)