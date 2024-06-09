import discord
from discord.ext import commands
from src.yiffs import InfoCommands, InteractCommands, UserCommands, DefineSettings, DefineAI, FunCommands, ModCommands
from src.yiffs.events import OnReadyEvent, OnMessageEvent, OnMessageDeleteEvent, OnMessageEditEvent, OnMemberUpdate, OnMemberJoin, OnMemberRemove, OnVoiceStateUpdate
from src.services.BotService import bot
from src.services.SettingsService import settings

# Set the guilds
guild = discord.Object(id=settings.GUILD)

# Add the commands to the bot
bot.tree.add_command(InfoCommands.info(bot), guild=guild)
bot.tree.add_command(InteractCommands.interact(bot), guild=guild)
bot.tree.add_command(UserCommands.user(bot), guild=guild)
bot.tree.add_command(DefineSettings.settings(bot), guild=guild)
bot.tree.add_command(DefineAI.ai(bot), guild=guild)
bot.tree.add_command(FunCommands.fun(bot), guild=guild)
bot.tree.add_command(ModCommands.mod(bot), guild=guild)

## Run the bot
if __name__ == "__main__":
    bot.run(settings.TOKEN)