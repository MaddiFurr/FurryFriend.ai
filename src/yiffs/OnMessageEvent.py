from ..bot import bot



@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    ## Replace Twitter Links with VXTwitter Links
    if "https://twitter.com" in message.content:
        await message.channel.send("Here let me help!\n{} Sent the below message that had a Twitter link that needed fixing :)\n\n".format(message.author.name) + "<@{}>:\n> ".format(message.author.id) + message.content.replace("https://twitter.com/","https://vxtwitter.com/"))
        await message.delete()
        print("Replaced {} with VXTwitter Link".format(message.content))
    if "https://x.com/" in message.content:
        await message.channel.send("Here let me help!\n{} Sent the below message that had a Twitter link that needed fixing :)\n\n".format(message.author.name) + "<@{}>:\n> ".format(message.author.id) + message.content.replace("https://x.com/","https://vxtwitter.com/"))
        await message.delete()
        print("Replaced {} with VXTwitter Link".format(message.content))
    await bot.process_commands(message)