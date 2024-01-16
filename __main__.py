import discord
from discord.ext import commands
from src.yiffs import OnReadyEvent, OnMessageEvent, InfoCommands, InteractCommands, UserCommands
from src.services.BotService import bot
from src.services.SettingsService import settings

# Set the guilds
guild = discord.Object(id=settings.GUILD)

# Add the commands to the bot
bot.tree.add_command(InfoCommands.info(bot), guild=guild)
bot.tree.add_command(InteractCommands.interact(bot), guild=guild)
bot.tree.add_command(UserCommands.user(bot), guild=guild)

## Run the bot
if __name__ == "__main__":
    bot.run(settings.TOKEN)