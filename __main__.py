import discord
from discord.ext import commands
from src.yiffs import OnMessageEvent, InfoCommands, InteractCommands, UserCommands
from src.services.BotService import bot
import configparser

# Set the guilds
guilds = [discord.Object(id) for id in ["907855215137554442"]] #, "917618961124851732"

# Add the commands to the bot
for guild_id in guilds:
    bot.tree.add_command(InfoCommands.info(bot), guild=guild_id)
    bot.tree.add_command(InteractCommands.interact(bot), guild=guild_id)
    bot.tree.add_command(UserCommands.user(bot), guild=guild_id)

## Once the bot is ready, sync the commands to the guild, and print a ready message
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Here to touch on your anal cavity :3"), status=discord.Status.online)
    for guild_id in guilds:
        await bot.tree.sync(guild=guild_id)
    permissions = discord.Intents.all()
    url = f"https://discord.com/oauth2/authorize?client_id={bot.user.id}&permissions={permissions.value}&scope=bot"
    print(f"Bot is ready! Add it to your server using this link: {url}")

# Load bot configuration from bot.conf
config = configparser.ConfigParser()
config.read("bot.conf")
TOKEN = config.get("Bot", "TOKEN")

## Run the bot
if __name__ == "__main__":
    bot.run(TOKEN)