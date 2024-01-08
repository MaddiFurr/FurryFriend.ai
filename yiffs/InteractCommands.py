import discord
from discord import app_commands as apc
from discord import Webhook
from discord import Webhook

class interact(apc.Group):
    """Manage general commands"""
    def __init__(self, bot: discord.ext.commands.Bot):
        super().__init__()
        self.bot = bot

    @apc.command()
    async def pet(self, interaction: discord.Interaction, user: discord.User):
        #send_webhook_message(interaction.guild, interaction.channel, interaction.user, "pet {}".format(user), "pet")
        await interaction.response.send_message('You pet <@{}>'.format(user.id), ephemeral=True)
        send_webhook_message(interaction.guild, interaction.channel, interaction.user, "*pets <@{}>".format(user.id), "pet")
        print("{} ({}) pet {} ({})".format(interaction.user.name, interaction.user.id, user, user.id))



async def send_webhook_message(server, channel, sender, message: str, webhook_name: str):
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