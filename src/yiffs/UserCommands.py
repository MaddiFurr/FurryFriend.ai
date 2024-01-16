import discord
from discord import app_commands as apc
from ..services.PermissionChecker import permission_checker
from .usercommands.status import status
from .usercommands.account import account
from .usercommands.permissions import permissions
from .usercommands.roles import roles

class user(apc.Group):
    """Manage general commands"""
    def __init__(self, bot: discord.ext.commands.Bot):
        super().__init__()
        self.bot = bot
    
    # Get a user's status and activities
    @apc.command()
    async def status(self, interaction: discord.Interaction, user: discord.User):
        """Get a user's status and activities"""
        await status(interaction, user)
    
    # Get a user's account information
    @apc.command()
    async def account(self, interaction: discord.Interaction, user: discord.User):
        """Get a user's account information"""
        await account(interaction, user)
    
    # Get a user's permissions
    @apc.command()
    async def permissions(self, interaction: discord.Interaction, user: discord.User):
        """Get a user's permissions"""
        await permissions(interaction, user)
    
    # Get a user's roles
    @apc.command()
    async def roles(self, interaction: discord.Interaction, user: discord.User):
        """Get a user's roles"""
        await roles(interaction, user)