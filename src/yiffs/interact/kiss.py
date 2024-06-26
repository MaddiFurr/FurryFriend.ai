import discord
from discord import app_commands as apc
from ...services.BotService import bot
from ...services.WebhookService import send_webhook_message
from ...services.LoggingService import log
import random

async def kiss(interaction: discord.Interaction, user: discord.User):
        """Kiss a user!"""
        
        intensity = random.choice(["tenderly", "lovingly", "softly", "affectionately", "passionately", "gently"])
        kiss_type = random.choice(["kisses", "smooches", "pecks"])
        
        # Check if the user is trying to pet themselves
        if user.id == interaction.user.id:
            await interaction.response.send_message("You can't kiss yourself ya silly! But I'll kiss you instead!\n\n*{} {} <@{}>*".format(intensity, kiss_type, interaction.user.id), ephemeral=False)
            await log(None, "{} ({}) tried to kiss themselves. I kissed them instead.".format(interaction.user.name,interaction.user.id), "/interact kiss <self>", interaction.user, interaction.channel)
            return
        
        # Check if the user is trying to pet the bot
        if user.id == bot.user.id:
            await interaction.response.send_message("You can't kiss me ya silly!", ephemeral=False)
            await log(None, "{} ({}) tried to kiss me. I can't be kissed!".format(interaction.user.name,interaction.user.id), "/interact kiss <bot>", interaction.user, interaction.channel)
            return
        
        # Pet the user specified
        await send_webhook_message(interaction.guild, interaction.channel, interaction.user, "*{} {} <@{}>*".format(intensity, kiss_type, user.id))
        await interaction.response.send_message("Sent your kiss to <@{}>".format(user.id), ephemeral=True)
        await log(None, "{} ({}) has kissed <@{}>.".format(interaction.user.name,interaction.user.id,user.id), "/interact kiss", interaction.user, interaction.channel)
        