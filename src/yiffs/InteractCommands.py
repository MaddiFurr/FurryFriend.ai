import discord
from discord import app_commands as apc
from ..services.BotService import bot
from ..services.WebhookService import send_webhook_message
from .interact.pet import pet

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