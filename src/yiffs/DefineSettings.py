import discord
from discord import app_commands as apc
from ..services.BotService import bot
from .settings.botstatus import botstatus
from .settings.setjoinrole import setjoinrole

class settings(apc.Group):
    """Manage general commands"""
    def __init__(self, bot: discord.ext.commands.Bot):
        super().__init__()
        self.bot = bot
    
    # Change the bot's status
    @apc.command()
    async def botstatus(self, interaction: discord.Interaction, newstatus: str):
        """Change the bot's status"""
        await botstatus(interaction, newstatus)
        
    # Set the role assigned to users upon joining
    #@apc.command()
    #async def setjoinrole(self, interaction: discord.Interaction, newrole: str):
    #    """Set the role assigned to users upon joining"""
    #    await setjoinrole(interaction, newrole)