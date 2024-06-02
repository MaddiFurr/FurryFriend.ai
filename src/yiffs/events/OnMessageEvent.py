from ...services.BotService import bot
from ...services.WebhookService import send_webhook_message
from ...services.LoggingService import log

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    ## Replace Twitter Links with TwittPR Links
    if "https://twitter.com" in message.content:
        await send_webhook_message(message.guild, message.channel, message.author, message.content.replace("https://twitter.com/","https://twittpr.com/"))
        await message.delete()
        await log(None, f"Replaced {message.content} with TwittPR Link", None, None, message.channel)
    if "https://x.com/" in message.content:
        await send_webhook_message(message.guild, message.channel, message.author, message.content.replace("https://x.com/","https://twittpr.com/"))
        await message.delete()
        await log(None, f"Replaced {message.content} with TwittPR Link", None, None, message.channel)
    await bot.process_commands(message)
    
    await log(None, None, "on_message", message.author, message.channel)