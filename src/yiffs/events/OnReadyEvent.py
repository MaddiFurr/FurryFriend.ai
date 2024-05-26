import discord
from ...services.BotService import bot
from ...services.SettingsService import settings
from ...services.LoggingService import log


guild = discord.Object(id=settings.GUILD)

## Once the bot is ready, sync the commands to the guild, and print a ready message
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=settings.STATUS), status=discord.Status.online)
    await bot.tree.sync(guild=guild)
    permissions = discord.Intents.all()
    url = f"https://discord.com/oauth2/authorize?client_id={bot.user.id}&permissions={permissions.value}&scope=bot"
    await log(None, f"Bot is ready! Now in {len(bot.guilds)} guilds. [Invite me!]({url})", None, None, None)