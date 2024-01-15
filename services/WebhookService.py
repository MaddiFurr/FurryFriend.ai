import discord
from discord import Webhook, RequestsWebhookAdapter

async def send_webhook_message(server, channel, sender: User, message: str, webhook_name: str):
    # Get the list of webhooks in the channel
    webhooks = await channel.webhooks()

    # Check if the webhook already exists
    webhook = discord.utils.get(webhooks, name=webhook_name)

    # If the webhook does not exist, create it
    if not webhook:
        webhook = await channel.create_webhook(name=webhook_name)

    # Set the webhook's avatar to be the same as the sender's avatar
    if sender.avatar_url:
        await webhook.edit(avatar=await sender.avatar_url.read())

    # Send the message
    await webhook.send(content=message, username=sender.name, avatar_url=sender.avatar_url)