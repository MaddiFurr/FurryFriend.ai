import discord
from discord import app_commands as apc
from ..services.BotService import bot
from ..services.WebhookService import send_webhook_message
from .ai.singleprompt import single_prompt

class ai(apc.Group):
    """Manage AI commands"""
    def __init__(self, bot: discord.ext.commands.Bot):
        super().__init__()
        self.bot = bot
    
    # Get a user's status and activities
    @apc.command()
    async def single(self, interaction: discord.Interaction, prompt: str):
        """Prompt the AI!"""
        await single_prompt(interaction, prompt)
        