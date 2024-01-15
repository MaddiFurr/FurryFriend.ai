import discord
from discord.ext import commands
import yiffs.InfoCommands as InfoCommands
import yiffs.InteractCommands as InteractCommands
import yiffs.UserCommands as UserCommands
import configparser

# Load bot configuration from bot.conf
config = configparser.ConfigParser()
config.read("bot.conf")
TOKEN = config.get("Bot", "TOKEN")
GUILD_IDS = [discord.Object(id) for id in ["1192534770622681230", "917618961124851732"]]

## Create the bot
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.presences = True
intents.members = True
bot = commands.Bot(command_prefix=".",intents=intents)

# Add the commands to the bot
for guild_id in GUILD_IDS:
    bot.tree.add_command(InfoCommands.info(bot), guild=guild_id)
    bot.tree.add_command(InteractCommands.interact(bot), guild=guild_id)
    bot.tree.add_command(UserCommands.user(bot), guild=guild_id)

## Once the bot is ready, sync the commands to the guild, and print a ready message
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Here to touch on your anal cavity :3"), status=discord.Status.online)
    for guild_id in GUILD_IDS:
        await bot.tree.sync(guild=guild_id)
    permissions = discord.Intents.all()
    url = f"https://discord.com/oauth2/authorize?client_id={bot.user.id}&permissions={permissions.value}&scope=bot"
    print(f"Bot is ready! Add it to your server using this link: {url}")

## If a message is sent, check if it contains a twitter link, and if so, replace it with a VXTwitter link
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "https://twitter.com" in message.content:
        await message.channel.send(message.content.replace("https://twitter.com/","https://vxtwitter.com/"))
        await message.delete()
        print("Replaced {} with VXTwitter Link".format(message.content))
    if "https://x.com/" in message.content:
        await message.channel.send(message.content.replace("https://x.com/","https://vxtwitter.com/"))
        await message.delete()
        print("Replaced {} with VXTwitter Link".format(message.content))
    await bot.process_commands(message)

## Run the bot
if __name__ == "__main__":
    bot.run(TOKEN)

#@bot.tree.command(guild=MY_GUILD, name="hi",description="This is a test hello command")
#async def slash_command(interaction:discord.Interaction):
#    await interaction.response.send_message("Hello World!")