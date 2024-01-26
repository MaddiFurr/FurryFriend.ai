import discord
from discord import app_commands as apc
from ...services.BotService import bot
from ...services.WebhookService import send_webhook_message
import random

async def hug(interaction: discord.Interaction, user: discord.User):
        """Hug a user!"""
        
        intensity = random.choice(["tightly", "tenderly", "lovingly", "softly", "affectionately", "firmly", "gently"])
        hug_type = random.choice(["hugs", "embraces", "squeezes", "cuddles", "snuggles", "holds", "cradles"])
        
        # Check if the user is trying to pet themselves
        if user.id == interaction.user.id:
            await interaction.response.send_message("You can't hug yourself ya silly! But I'll hug you instead!\n\n*{} {} <@{}>*".format(intensity, hug_type, interaction.user.id), ephemeral=False)
            return
        
        # Check if the user is trying to pet the bot
        if user.id == bot.user.id:
            await interaction.response.send_message("You can't hug me ya silly!", ephemeral=False)
            return
        
        # Pet the user specified
        await send_webhook_message(interaction.guild, interaction.channel, interaction.user, "*{} {} <@{}>*".format(intensity, hug_type, user.id))
        await interaction.response.send_message("Sent your hug to <@{}>".format(user.id), ephemeral=True)
        