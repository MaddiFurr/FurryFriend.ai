import discord
from ...services.BotService import bot
from ...services.SettingsService import settings
from ...services.LoggingService import log
import time

## On a message edit event, send an embed to the log channel
@bot.event
async def on_message_edit(message_before, message_after):
    # Don't log webhook messages
    if message_before.webhook_id:
        return
    
    # This was added because for some reason, a log was being created when a message with an embed
    # Because Ciscord thinks that the message was edited, even though it wasn't
    if message_after.content == message_before.content:
        return
    
    epoch = int(time.time())
    e = discord.Embed(title="Message Edited", description=f"Message edited in {message_before.channel.mention}", color=0xf1c40f)
    e.add_field(name="Action Severity", value="1 - Low", inline=False)
    e.add_field(name="Author", value=message_before.author.mention, inline=False)
    e.add_field(name="Before Edit", value=message_before.content, inline=True)
    e.add_field(name="After Edit", value=message_after.content, inline=True)
    e.add_field(name="Jump to Message", value=f"[Click Here]({message_before.jump_url})", inline=False)
    e.add_field(name="Occurred at", value="<t:{}>".format(str(epoch)), inline=False)
    await log(e, f"Message edited in {message_before.channel.mention} || {message_before.author.mention}: {message_before.content} -> {message_after.content}", "on_message_edit", message_before.author,message_before.channel)
    