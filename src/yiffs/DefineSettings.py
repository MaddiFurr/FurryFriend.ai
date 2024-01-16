import discord
from discord import app_commands as apc
from ..services.BotService import bot
from ..services.PermissionChecker import permission_checker
from .settings.logchannel import update_logchannel

class settings(apc.Group):
    """Manage general commands"""
    def __init__(self, bot: discord.ext.commands.Bot):
        super().__init__()
        self.bot = bot
    
    # Say hello to the bot!
    @apc.command()
    async def logchannel(self, interaction: discord.Interaction, channel: discord.TextChannel):
        """Change the guild's log channel"""
        user = interaction.user
        await update_logchannel(interaction, user, channel)
        