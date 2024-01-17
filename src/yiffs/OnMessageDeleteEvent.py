import discord
from ..services.BotService import bot
from ..services.SettingsService import settings
import time

## On a message delete event, send an embed to the log channel
@bot.event
async def on_message_delete(message):
    epoch = int(time.time())
    e = discord.Embed(title="Message Deleted", description=f"Message deleted in {message.channel.mention}", color=0xe74c3c)
    e.add_field(name="Action Severity", value="2 - Low/Medium", inline=False)
    e.add_field(name="Author", value=message.author.mention, inline=True)
    e.add_field(name="Message", value=message.content, inline=True)
    e.add_field(name="Occurred at", value="<t:{}>".format(str(epoch)), inline=False)
    loggingchannel = bot.get_channel(int(settings.LOG_CHANNEL))
    await loggingchannel.send(embed=e)
    print(f"Message deleted in {message.channel.mention} || {message.author.mention}: {message.content}")
    