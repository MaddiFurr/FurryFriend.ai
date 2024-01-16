import discord
from ..services.BotService import bot
from ..services.SettingsService import settings


guild = discord.Object(id=settings.GUILD)

## Once the bot is ready, sync the commands to the guild, and print a ready message
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=settings.STATUS), status=discord.Status.online)
    await bot.tree.sync(guild=guild)
    permissions = discord.Intents.all()
    url = f"https://discord.com/oauth2/authorize?client_id={bot.user.id}&permissions={permissions.value}&scope=bot"
    print(f"Bot is ready! Add it to your server using this link: {url}")