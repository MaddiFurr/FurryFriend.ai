import discord
from discord.ext import commands
import yiffs.TestCommands as TestCommands
import configparser

# Load bot configuration from bot.conf
config = configparser.ConfigParser()
config.read("bot.conf")
TOKEN = config.get("Bot", "TOKEN")
MY_GUILD = discord.Object(907855215137554442)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=".",intents=intents)

@bot.tree.command(guild=MY_GUILD, name="hi",description="This is a test hello command")
async def slash_command(interaction:discord.Interaction):
    await interaction.response.send_message("Hello World!")

bot.tree.add_command(TestCommands.Generalgroup(bot), guild=MY_GUILD)


@bot.event
async def on_ready():
    await bot.tree.sync(guild=MY_GUILD)


bot.run(TOKEN)
