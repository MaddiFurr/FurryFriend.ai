import discord
from discord import app_commands as apc
from ..services.BotService import bot
from ..services.PermissionChecker import permission_checker
from .info.hello import hello
from .info.version import version
from .info.botstatus import botstatus

class info(apc.Group):
    """Manage general commands"""
    def __init__(self, bot: discord.ext.commands.Bot):
        super().__init__()
        self.bot = bot
    
    # Say hello to the bot!
    @apc.command()
    async def hello(self, interaction: discord.Interaction):
        """Say "hello" to the bot!"""
        await hello(interaction)
    
    # Get the bot's Version
    @apc.command()
    async def version(self, interaction: discord.Interaction):
        """Tells you what version of the bot software is running."""
        await version(interaction)
    
    # Change the bot's status
    @apc.command()
    async def botstatus(self, interaction: discord.Interaction, newstatus: str):
        """Change the bot's status"""
        await botstatus(interaction, newstatus)
        