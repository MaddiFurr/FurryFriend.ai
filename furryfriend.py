import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

#read the bot token from the client.token file
with open('client.token') as f:
    token = f.readline()

# Define the folder path where your cogs are located
cogs_folder = 'cogs'

# Get the list of files in the cogs folder
cog_files = [file for file in os.listdir(cogs_folder) if file.endswith('.py')]

# Load each cog
async def load_cogs():
    for cog in cog_files:
        # Remove the file extension to get the cog name
        cog_name = cog[:-3]
        # Construct the full module path
        module = f"{cogs_folder}.{cog_name}"
        
        try:
            bot.load_extension(module)  # Load the cog using load_extension method
            print(f"Loaded {module}")
        except Exception as e:
            print(f"Failed to load {module}. Error: {str(e)}")

# Run your bot and load cogs
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} ({bot.user.id})")
    await load_cogs()  # Await the load_cogs function

bot.run(token)