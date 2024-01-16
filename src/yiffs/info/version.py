import discord
from discord import app_commands as apc
from ...services.BotService import bot
from ...services.PermissionChecker import permission_checker


async def version(interaction: discord.Interaction):
        """Tells you what version of the bot software is running."""
        await interaction.response.send_message('Bot Running: DEV 0.0.1', ephemeral=True)
        print("Version command ran by {} ({})".format(interaction.user.name,interaction.user.id))