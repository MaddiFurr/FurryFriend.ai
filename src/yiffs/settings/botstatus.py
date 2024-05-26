import discord
from discord import app_commands as apc
from ...services.BotService import bot
from ...services.PermissionChecker import permission_checker
from ...services.LoggingService import log


async def botstatus(interaction: discord.Interaction, newstatus: str):
        """Change the bot's status"""
        if await permission_checker(interaction.user, 'admin') == False:
            await interaction.response.send_message("You don't have permission to run this command!", ephemeral=True)
            await log(None, "{} ({}) tried to run the botstatus command without permission.".format(interaction.user.name,interaction.user.id), "/settings botstatus <NoPerms>", interaction.user, interaction.channel)
            return
        
        await bot.change_presence(activity=discord.Game(name=newstatus), status=discord.Status.online)
        await interaction.response.send_message('Bot status changed to:\n`{}`'.format(newstatus), ephemeral=True)
        print("Bot Status command ran by {} ({}). Changed status to: {}".format(interaction.user.name,interaction.user.id, newstatus))
        await log(None, "{} ({}) has run the botstatus command. Changed status to: {}".format(interaction.user.name,interaction.user.id, newstatus), "/settings botstatus", interaction.user, interaction.channel)