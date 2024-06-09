from ...services.BotService import bot
from ...services.WebhookService import send_webhook_message
from ...services.LoggingService import log
from ...services.ModActionService import create_mod_action
from ...services.GeminiService import single
from ...services.DBService import get_user_field, update_user_field
import os
from datetime import datetime, timedelta

# Read the text file and create a dictionary of words and definitions
dir_path = os.path.dirname(os.path.realpath(__file__))
word_definitions = {}
with open(os.path.join(dir_path, '../../../configs/badwords.txt'), 'r') as file:
    for line in file:
        word, definition = line.strip().split('&:')
        word_definitions[word] = definition

with open(os.path.join(dir_path, '../../../configs/aimoderationprompt.txt'), 'r', encoding='utf-8') as file:
    for line in file:
        community_guidelines = line.strip()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    ## Replace Twitter Links with TwittPR Links
    if "https://twitter.com" in message.content:
        await send_webhook_message(message.guild, message.channel, message.author, message.content.replace("https://twitter.com/","https://fixup.com/"))
        await message.delete()
        await log(None, f"Replaced {message.content} with FixupX Link", None, None, message.channel)
    if "https://x.com/" in message.content:
        await send_webhook_message(message.guild, message.channel, message.author, message.content.replace("https://x.com/","https://fixup.com/"))
        await message.delete()
        await log(None, f"Replaced {message.content} with FixupX Link", None, None, message.channel)
    await bot.process_commands(message)
    
    await log(None, None, "on_message", message.author, message.channel)
    
    prompt_start = """Please moderate the User Message below.
    You are doing a quick sentiment analysis on the message a human being will do a final look over the message.
    Only return the text 'Action Recommended' or 'No Action Needed'."""
    
    for word, definition in word_definitions.items():
            if word in message.content.lower():
                
                
                full_prompt = f"{prompt_start}\n\nUser Message: {message.content}"
                AI_RESPONSE = await single(full_prompt)
                
                # The word is in the message, so trigger an action
                if 'text' in AI_RESPONSE:
                    await create_mod_action(message.channel, message.id, "moderator", f"\nThe AI detected the word: **'{word}'** which means: **{definition}**", AI_RESPONSE.text)
                else:
                    await create_mod_action(message.channel, message.id, "moderator", f"\nThe AI detected the word: **'{word}'** which means: **{definition}**", "> *The AI did not respond with reasoning which means that the message will probably violate Community Guidelines*")
                
                break