import discord
from discord import Webhook
from .BotService import bot

async def send_webhook_message(server, channel, sender: discord.User, message: str):
    webhook_name = "FurryFriendAI_Webhook"
    # Get the list of webhooks in the channel
    webhooks = await channel.webhooks()

    # Check if the user is not None
    if sender is not None:
        avatar = str(sender.avatar)
        display_name = sender.display_name
    else:
        avatar = 'Default avatar'
        display_name = 'Unknown user'
        
    # Check if the webhook already exists
    webhook = discord.utils.get(webhooks, name=webhook_name)

    # If the webhook does not exist, create it
    if not webhook:
        webhook = await channel.create_webhook(name=webhook_name)
    
    # Send the message
    await webhook.send(content=message, username=display_name, avatar_url=avatar)