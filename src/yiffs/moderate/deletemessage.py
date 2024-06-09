import discord
from discord import app_commands as apc
from ...services.BotService import bot
from ...services.PermissionChecker import permission_checker
from ...services.WebhookService import send_webhook_message
from ...services.LoggingService import log
from ...services.DBService import get_user_field, update_user_field

async def delete_message(interaction: discord.Interaction, message_id: str, reason: str):
    """Delete a single message"""
    if await permission_checker(interaction.user, 'mod') == False:
        await interaction.response.send_message("You don't have permission to run this command!", ephemeral=True)
        return

    try:
        # Fetch the message by its ID
        message = await interaction.channel.fetch_message(int(message_id))
    except discord.NotFound:
        await interaction.response.send_message("Message not found! Ensure you use this command in the same channel as the message you are trying to delete!", ephemeral=True)
        return

    # Send a message to the author of the message
    dme = discord.Embed(title="Message Deleted", description=f"Your message in {message.channel.mention} was deleted.", color=0xe74c3c)
    dme.add_field(name="Message", value=message.content, inline=False)
    dme.add_field(name="Reason", value=reason, inline=False)
    dme.add_field(name="Occurred at", value="<t:{}>".format(str(int(message.created_at.timestamp()))), inline=False)
    dme.add_field(name="Reference ID", value=f"{message.channel.id}:{message.id}", inline=False)
    dme.set_footer(text="If you have any questions or concerns, please contact the moderators with the Reference ID above.")
    
    try:
        await message.author.send(embed=dme)
    except discord.Forbidden:
        await interaction.response.send_message("Message deleted, but I couldn't DM the user to notify them.", ephemeral=True)
        return

    e = discord.Embed(title="Message Deleted By Mod", description=f"Message deleted in {message.channel.mention}", color=0xe74c3c)
    e.add_field(name="Action Severity", value="2 - Low/Medium", inline=False)
    e.add_field(name="Author", value=message.author.mention, inline=True)
    e.add_field(name="Message", value=message.content, inline=True)
    e.add_field(name="Deleted by", value=interaction.user.mention, inline=True)
    e.add_field(name="Reason", value=reason, inline=False)
    e.add_field(name="Occurred at", value="<t:{}>".format(str(int(message.created_at.timestamp()))), inline=False)
    e.set_footer(text=f"Reference ID: {message.channel.id}:{message.id}")
    # Log the deletion
    await log(e,f"Message deleted by {interaction.user.name} ({interaction.user.id}) on user {message.author.name} ({message.author.id}) in {message.channel.name} ({message.channel.id}) for reason: {reason}",None,message.author,message.channel)
    
    actions = await get_user_field(interaction.user.id, "mod_actions.delete_message")
    print(actions)
    if actions is None:
        actions = 0
    actions = actions + 1
    print(actions)
    await update_user_field(interaction.user.id, "mod_actions.delete_message", actions)
    
    # Delete the message
    await message.delete()
    await interaction.response.send_message("Message deleted!", ephemeral=True)