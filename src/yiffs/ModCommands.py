import discord
from discord import app_commands as apc
from discord import Message
from ..services.BotService import bot
from ..services.WebhookService import send_webhook_message
from .moderate.deletemessage import delete_message


# eventually go back and fix this to be in one python file you fucking goober

class mod(apc.Group):
    """Manage Moderator commands"""
    def __init__(self, bot: discord.ext.commands.Bot):
        super().__init__()
        self.bot = bot
    
    # The delete message
    @apc.command()
    async def delete(self, interaction: discord.Interaction, message: str, reason: str):
        """Pet a user!"""
        await delete_message(interaction, message)

        