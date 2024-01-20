from ...services.BotService import bot
from ...services.WebhookService import send_webhook_message

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    ## Replace Twitter Links with TwittPR Links
    if "https://twitter.com" in message.content:
        await send_webhook_message(message.guild, message.channel, message.author, message.content.replace("https://twitter.com/","https://twittpr.com/"))
        await message.delete()
        print("Replaced {} with TwittPR Link".format(message.content))
    if "https://x.com/" in message.content:
        await send_webhook_message(message.guild, message.channel, message.author, message.content.replace("https://x.com/","https://twittpr.com/"))
        await message.delete()
        print("Replaced {} with TwittPR Link".format(message.content))
    await bot.process_commands(message)