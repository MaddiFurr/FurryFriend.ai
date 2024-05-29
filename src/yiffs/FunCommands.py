import discord
from discord import app_commands as apc
from ..services.BotService import bot
from ..services.WebhookService import send_webhook_message
from .fun.eight_ball import eight_ball

class fun(apc.Group):
    """Manage fun commands"""
    def __init__(self, bot: discord.ext.commands.Bot):
        super().__init__()
        self.bot = bot

    @apc.command(name="8ball", description="Ask the Magic 8-Ball a question!")
    async def eight_ball(self, interaction: discord.Interaction, question: str):
        """Change the bot's status"""
        await eight_ball(interaction, question)
        