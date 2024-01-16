import discord
from discord import app_commands as apc
from ..services.BotService import bot
from ..services.WebhookService import send_webhook_message

class interact(apc.Group):
    """Manage general commands"""
    def __init__(self, bot: discord.ext.commands.Bot):
        super().__init__()
        self.bot = bot

    @apc.command()
    async def pet(self, interaction: discord.Interaction, user: discord.User):
        """Pet a user!"""
        # Check if the user is trying to pet themselves
        if user.id == interaction.user.id:
            await interaction.response.send_message("You can't pet yourself ya silly! But I'll pet you instead!\n\n*gently pets <@{}>*".format(interaction.user.id), ephemeral=False)
            return
        
        # Check if the user is trying to pet the bot
        if user.id == bot.user.id:
            await interaction.response.send_message("You can't pet me ya silly!", ephemeral=True)
            return
        
        # Pet the user specified
        await send_webhook_message(interaction.guild, interaction.channel, interaction.user, "*gently pets <@{}>*".format(user.id))
        await interaction.response.send_message("You pet <@{}>".format(user.id), ephemeral=True)