import discord
from discord.ext import commands
import yiffs.InfoCommands as InfoCommands
import yiffs.InteractCommands as InteractCommands
import configparser

# Load bot configuration from bot.conf
config = configparser.ConfigParser()
config.read("bot.conf")
TOKEN = config.get("Bot", "TOKEN")
MY_GUILD = discord.Object(config.get("Bot", "GUILD"))

## Create the bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=".",intents=intents)

## Add the commands to the bot
bot.tree.add_command(InfoCommands.info(bot), guild=MY_GUILD)
bot.tree.add_command(InteractCommands.interact(bot), guild=MY_GUILD)

## Once the bot is ready, sync the commands to the guild, and print a ready message
@bot.event
async def on_ready():
    await bot.tree.sync(guild=MY_GUILD)
    print("Bot is ready! {} {}".format(bot.user.name,bot.user.id))

## Run the bot
if __name__ == "__main__":
    bot.run(TOKEN)

#@bot.tree.command(guild=MY_GUILD, name="hi",description="This is a test hello command")
#async def slash_command(interaction:discord.Interaction):
#    await interaction.response.send_message("Hello World!")