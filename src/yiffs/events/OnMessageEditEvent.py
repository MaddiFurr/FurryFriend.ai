import discord
from ...services.BotService import bot
from ...services.SettingsService import settings
import time

## On a message edit event, send an embed to the log channel
@bot.event
async def on_message_edit(message_before, message_after):
    if message_before.webhook_id:
        return
    epoch = int(time.time())
    e = discord.Embed(title="Message Edited", description=f"Message edited in {message_before.channel.mention}", color=0xf1c40f)
    e.add_field(name="Action Severity", value="1 - Low", inline=False)
    e.add_field(name="Author", value=message_before.author.mention, inline=False)
    e.add_field(name="Before Edit", value=message_before.content, inline=True)
    e.add_field(name="After Edit", value=message_after.content, inline=True)
    e.add_field(name="Jump to Message", value=f"[Click Here]({message_before.jump_url})", inline=False)
    e.add_field(name="Occurred at", value="<t:{}>".format(str(epoch)), inline=False)
    loggingchannel = bot.get_channel(int(settings.LOG_CHANNEL))
    await loggingchannel.send(embed=e)
    print(f"Message edited in {message_before.channel.mention} || {message_before.author.mention}: {message_before.content} -> {message_after.content}")
    