import discord
from discord import app_commands as apc
from ...services.BotService import bot
from ...services.WebhookService import send_webhook_message
import random

async def pet(interaction: discord.Interaction, user: discord.User):
        """Pet a user!"""
        
        intensity = random.choice(["gently", "roughly", "softly", "playfully", "lovingly", "tenderly", "affectionately", "firmly", "slowly", "quickly", "passionately"])
        pet_type = random.choice(["pets", "rubs", "strokes", "caresses", "pats"])
        
        # Check if the user is trying to pet themselves
        if user.id == interaction.user.id:
            await interaction.response.send_message("You can't pet yourself ya silly! But I'll pet you instead!\n\n*{} {} <@{}>*".format(intensity, pet_type, interaction.user.id), ephemeral=False)
            return
        
        # Check if the user is trying to pet the bot
        if user.id == bot.user.id:
            await interaction.response.send_message("You can't pet me ya silly!", ephemeral=False)
            return
        
        # Pet the user specified
        await send_webhook_message(interaction.guild, interaction.channel, interaction.user, "*{} {} <@{}>*".format(intensity, pet_type, user.id))
        await interaction.response.send_message("Sent your pet to <@{}>".format(user.id), ephemeral=True)
        