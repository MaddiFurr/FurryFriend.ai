import discord
from discord import app_commands as apc
from ..services.BotService import bot
from ..services.WebhookService import send_webhook_message
from .interact.pet import pet
from .interact.hug import hug
from .interact.kiss import kiss

# eventually go back and fix this to be in one python file you fucking goober

class interact(apc.Group):
    """Manage general commands"""
    def __init__(self, bot: discord.ext.commands.Bot):
        super().__init__()
        self.bot = bot
    
    # The pet command
    @apc.command()
    async def pet(self, interaction: discord.Interaction, user: discord.User):
        """Pet a user!"""
        await pet(interaction, user)
    
    # The hug command
    @apc.command()
    async def hug(self, interaction: discord.Interaction, user: discord.User):
        """Hug a user!"""
        await hug(interaction, user)
    
    # The kiss command
    @apc.command()
    async def kiss(self, interaction: discord.Interaction, user: discord.User):
        """Kiss a user!"""
        await kiss(interaction, user)
        