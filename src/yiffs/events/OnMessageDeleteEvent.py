import discord
from ...services.BotService import bot
from ...services.SettingsService import settings
from ...services.LoggingService import log
import time

## On a message delete event, send an embed to the log channel
@bot.event
async def on_message_delete(message):
    epoch = int(time.time())
    
    if "https://twitter.com/" in message.content:
        e = discord.Embed(title="Message Deleted (Twitter.com)", description=f"Message deleted in {message.channel.mention}", color=0xe74c3c)
        e.add_field(name="Action Severity", value="0 - Low/Medium", inline=False)
    elif "https://x.com/" in message.content:
        e = discord.Embed(title="Message Deleted (X.com)", description=f"Message deleted in {message.channel.mention}", color=0xe74c3c)
        e.add_field(name="Action Severity", value="0 - Low/Medium", inline=False)
    else:
        e = discord.Embed(title="Message Deleted", description=f"Message deleted in {message.channel.mention}", color=0xe74c3c)
        e.add_field(name="Action Severity", value="2 - Low/Medium", inline=False)
    
    e.add_field(name="Author", value=message.author.mention, inline=True)
    e.add_field(name="Message", value=message.content, inline=True)
    e.add_field(name="Occurred at", value="<t:{}>".format(str(epoch)), inline=False)
    await log(e, f"Message deleted in {message.channel.mention} || {message.author.mention}: {message.content}", "on_message_delete", message.author, message.channel)

    