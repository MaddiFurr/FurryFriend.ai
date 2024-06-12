import discord
from discord import app_commands as apc
from ..services.BotService import bot
from ..services.ModActionService import create_mod_action
from .settings.botstatus import botstatus
from .settings.dbupdate import dbupdate
from .settings.reactrole import add_reaction, remove_reaction
#from .settings.setjoinrole import setjoinrole

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
    
    # Add all users in a guild to the database
    @apc.command()
    async def dbupdate(self, interaction: discord.Interaction):
        """Add all users in a guild to the database"""
        await dbupdate(interaction)
    
    @apc.command()
    async def modaction(self, interaction: discord.Interaction, data: str, role: str):
        """Create a mod action"""
        print(f'We got to the await: {data}, {role}')
        await create_mod_action(data, role)
        
    @apc.command()
    async def add_reaction(self, interaction: discord.Interaction, emoji: str, message: str, role: str):
        """Add a reaction to a message"""
        await add_reaction(interaction, emoji, message, role)
        
    @apc.command()
    async def remove_reaction(self, interaction: discord.Interaction, message: str, role: str):
        """Remove a reaction from a message"""
        await remove_reaction(interaction, message, role)