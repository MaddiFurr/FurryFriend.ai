import discord
from discord import Webhook
from discord import NotFound, Forbidden
from .BotService import bot
from .SettingsService import settings
from .LoggingService import log
from .DBService import get_user_field, update_user_field
from .PermissionChecker import permission_checker
from datetime import datetime, timedelta

from discord import ui
from discord import Button, ButtonStyle, Embed
from discord.ext import commands

class ModActionService(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
        
    @discord.ui.button(label='Non-Action', style=discord.ButtonStyle.green)
    async def non_action(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'non-action'
        
        if not await permission_checker(interaction.user, 'mod') or not await permission_checker(interaction.user, 'admin'):
            await interaction.response.send_message("You do not have permission to do that!", ephemeral=True)
            return
        
        message = await interaction.channel.fetch_message(interaction.message.id)
        original_embed = message.embeds[0] if message.embeds else discord.Embed()        

        del_message = original_embed.footer.text.split(":")
        #print(del_message)
        channel_id = int(del_message[0])
        message_id = int(del_message[1])
        channel = interaction.guild.get_channel(channel_id)
        if channel is None:
            print(f"Channel {channel_id} not found")
            return
        finmessage = await channel.fetch_message(message_id)
        
        # Add the "Status" field to the original embed
        original_embed.add_field(name="Final Result", value="Not Actioned", inline=False)
        original_embed.add_field(name="Descision By", value=interaction.user.mention, inline=True)
        original_embed.color = 0x00ff00

        # Disable all the buttons
        for item in self.children:
            item.disabled = True

        # Edit the original message to update the embed and disable the buttons
        await message.edit(embed=original_embed, view=self)
        await interaction.response.send_message("Thank you for your response!", ephemeral=True)
        
        actions = await get_user_field(interaction.user.id, "mod_actions.non_action")
        if actions is None:
            actions = 0
        setactions = actions + 1
        await update_user_field(interaction.user.id, "mod_actions.non_action", setactions)

        
        self.stop()

    @discord.ui.button(label='Delete Message', style=discord.ButtonStyle.danger)
    async def delete_message(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'delete-message'
        
        if not await permission_checker(interaction.user, 'mod') or not await permission_checker(interaction.user, 'admin'):
            await interaction.response.send_message("You do not have permission to do that!", ephemeral=True)
            return
        
        message = await interaction.channel.fetch_message(interaction.message.id)

        # Get the original embed from the message, or create a new one if there are no embeds
        original_embed = message.embeds[0] if message.embeds else discord.Embed()

        del_message = original_embed.footer.text.split(":")
        #print(del_message)
        try:
            channel_id = int(del_message[0])
            message_id = int(del_message[1])
            channel = interaction.guild.get_channel(channel_id)
            if channel is None:
                print(f"Channel {channel_id} not found")
                return
            finmessage = await channel.fetch_message(message_id)
            try:
                await finmessage.author.send(f"Your message in {channel.mention} was deleted.\n\nIf you have any questions, please contact the moderators using Reference ID: ```{channel_id}:{message_id}```")
            except Forbidden:
                print(f"Bot does not have permission to DM user {finmessage.author.id}")
            await finmessage.delete()
            
        except ValueError:
            print(f"Invalid ID in footer: {original_embed.footer.text}")
        except NotFound:
            print(f"Message {message_id} not found in channel {channel_id}")
        except Forbidden:
            print(f"Bot does not have permission to delete message {message_id} in channel {channel_id}")
        
        # Add the "Status" field to the original embed
        original_embed.add_field(name="Final Result", value="Message Deleted & User Informed", inline=False)
        original_embed.add_field(name="Descision By", value=interaction.user.mention, inline=True)
        original_embed.color = 0x00ff00

        # Disable all the buttons
        for item in self.children:
            item.disabled = True
        
        # Edit the original message to update the embed and disable the buttons
        await message.edit(embed=original_embed, view=self)
        await interaction.response.send_message("Thank you for your response!", ephemeral=True)
        actions = await get_user_field(interaction.user.id, "mod_actions.delete_message")
        if actions is None:
            actions = 0
        setactions = actions + 1
        await update_user_field(interaction.user.id, "mod_actions.delete_message", setactions)
        self.stop()


    @discord.ui.button(label='Time Out User', style=discord.ButtonStyle.danger)
    async def time_out_user(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'time-out-user'
        await interaction.response.send_message("This feature is not yet implemented", ephemeral=True)
        return
        if not await permission_checker(interaction.user, 'mod') or not await permission_checker(interaction.user, 'admin'):
            await interaction.response.send_message("You do not have permission to do that!", ephemeral=True)
            return
        
        message = await interaction.channel.fetch_message(interaction.message.id)

        # Get the original embed from the message, or create a new one if there are no embeds
        original_embed = message.embeds[0] if message.embeds else discord.Embed()

        del_message = original_embed.footer.text.split(":")
        #print(del_message)
        try:
            channel_id = int(del_message[0])
            message_id = int(del_message[1])
            channel = interaction.guild.get_channel(channel_id)
            if channel is None:
                print(f"Channel {channel_id} not found")
                return
            finmessage = await channel.fetch_message(message_id)
            
            # Time out the user
            actions = await get_user_field(finmessage.author.id, "timeout_qty")
            if actions is None:
                actions = 0

            now = datetime.now()
            
            timeout_24_hours = now + timedelta(hours=24)
            timeout_7_days = now + timedelta(days=7)
            timeout_30_days = now + timedelta(days=30)
            
            # Calculate the durations
            duration_24_hours = timeout_24_hours - now
            duration_7_days = timeout_7_days - now
            duration_30_days = timeout_30_days - now

            # Format the durations
            str_24_hours = f"{duration_24_hours.days}d:{duration_24_hours.seconds // 3600}h:{(duration_24_hours.seconds % 3600) // 60}m:{duration_24_hours.seconds % 60}s"
            str_7_days = f"{duration_7_days.days}d:{duration_7_days.seconds // 3600}h:{(duration_7_days.seconds % 3600) // 60}m:{duration_7_days.seconds % 60}s"
            str_30_days = f"{duration_30_days.days}d:{duration_30_days.seconds // 3600}h:{(duration_30_days.seconds % 3600) // 60}m:{duration_30_days.seconds % 60}s"
            
            if actions == 0:
                await update_user_field(finmessage.author.id, "timeout_until", timeout_24_hours)
                await update_user_field(finmessage.author.id, "timeout_qty", actions + 1)
                await finmessage.author.send(f"Your message in {channel.mention} was deleted, and you have been timed out for {str_24_hours}\n\nIf you have any questions, please contact the moderators using Reference ID: ```{channel_id}:{message_id}```")
            elif actions == 1:
                await update_user_field(finmessage.author.id, "timeout_until", timeout_7_days)
                await update_user_field(finmessage.author.id, "timeout_qty", actions + 1)
                await finmessage.author.send(f"Your message in {channel.mention} was deleted, and you have been timed out for {str_7_days}\n\nIf you have any questions, please contact the moderators using Reference ID: ```{channel_id}:{message_id}```")
            elif actions == 2:
                await update_user_field(finmessage.author.id, "timeout_until", timeout_30_days)
                await update_user_field(finmessage.author.id, "timeout_qty", actions + 1)
                await finmessage.author.send(f"Your message in {channel.mention} was deleted, and you have been timed out for {str_30_days}\n\nIf you have any questions, please contact the moderators using Reference ID: ```{channel_id}:{message_id}```")
            
            setactions = actions + 1
            await update_user_field(finmessage.author.id, "timeout_until", setactions)
            
            
            
            await finmessage.delete()
        except ValueError:
            print(f"Invalid ID in footer: {original_embed.footer.text}")
        except NotFound:
            print(f"Message {message_id} not found in channel {channel_id}")
        except Forbidden:
            print(f"Bot does not have permission to delete message {message_id} in channel {channel_id}")
        
        # Add the "Status" field to the original embed
        original_embed.add_field(name="Final Result", value="Message Deleted & User Timmed Out", inline=False)
        original_embed.add_field(name="Descision By", value=interaction.user.mention, inline=True)
        original_embed.color = 0x00ff00

        # Disable all the buttons
        for item in self.children:
            item.disabled = True
        
        # Edit the original message to update the embed and disable the buttons
        await message.edit(embed=original_embed, view=self)
        await interaction.response.send_message("Thank you for your response!", ephemeral=True)
        
        actions = await get_user_field(interaction.user.id, "mod_actions.user_timeout")
        if actions is None:
            actions = 0
        setactions = actions + 1
        await update_user_field(interaction.user.id, "mod_actions.user_timeout", setactions)
        
        self.stop()

    @discord.ui.button(label='Kick User', style=discord.ButtonStyle.danger)
    async def kick_user(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'kick-user'
        
        if not await permission_checker(interaction.user, 'admin'):
            await interaction.response.send_message("You do not have permission to do that!", ephemeral=True)
            return
        
        message = await interaction.channel.fetch_message(interaction.message.id)

        # Get the original embed from the message, or create a new one if there are no embeds
        original_embed = message.embeds[0] if message.embeds else discord.Embed()

        del_message = original_embed.footer.text.split(":")
        #print(del_message)
        try:
            channel_id = int(del_message[0])
            message_id = int(del_message[1])
            channel = interaction.guild.get_channel(channel_id)
            if channel is None:
                print(f"Channel {channel_id} not found")
                return
            finmessage = await channel.fetch_message(message_id)
            await finmessage.author.kick(reason="User was kicked for violating community guidelines")
            await finmessage.delete()
        except ValueError:
            print(f"Invalid ID in footer: {original_embed.footer.text}")
        except NotFound:
            print(f"Message {message_id} not found in channel {channel_id}")
        except Forbidden:
            print(f"Bot does not have permission to delete message {message_id} in channel {channel_id}")
        
        # Add the "Status" field to the original embed
        original_embed.add_field(name="Final Result", value="Message Deleted & User Kicked", inline=False)
        original_embed.add_field(name="Descision By", value=interaction.user.mention, inline=True)
        original_embed.color = 0x00ff00

        # Disable all the buttons
        for item in self.children:
            item.disabled = True
        
        # Edit the original message to update the embed and disable the buttons
        await message.edit(embed=original_embed, view=self)
        await interaction.response.send_message("Thank you for your response!", ephemeral=True)
        
        actions = await get_user_field(interaction.user.id, "mod_actions.kick_user")
        if actions is None:
            actions = 0
        setactions = actions + 1
        await update_user_field(interaction.user.id, "mod_actions.kick_user", setactions)
        
        self.stop()

    @discord.ui.button(label='Ban User', style=discord.ButtonStyle.danger)
    async def ban_user(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'ban-user'
        
        if not await permission_checker(interaction.user, 'admin'):
            await interaction.response.send_message("You do not have permission to do that!", ephemeral=True)
            return
        
        message = await interaction.channel.fetch_message(interaction.message.id)

        # Get the original embed from the message, or create a new one if there are no embeds
        original_embed = message.embeds[0] if message.embeds else discord.Embed()

        del_message = original_embed.footer.text.split(":")
        #print(del_message)
        try:
            channel_id = int(del_message[0])
            message_id = int(del_message[1])
            channel = interaction.guild.get_channel(channel_id)
            if channel is None:
                print(f"Channel {channel_id} not found")
                return
            finmessage = await channel.fetch_message(message_id)
            await finmessage.author.ban(reason="User was banned for violating community guidelines")
            await finmessage.delete()
        except ValueError:
            print(f"Invalid ID in footer: {original_embed.footer.text}")
        except NotFound:
            print(f"Message {message_id} not found in channel {channel_id}")
        except Forbidden:
            print(f"Bot does not have permission to delete message {message_id} in channel {channel_id}")
        
        # Add the "Status" field to the original embed
        original_embed.add_field(name="Final Result", value="Message Deleted & User Banned", inline=False)
        original_embed.add_field(name="Descision By", value=interaction.user.mention, inline=True)
        original_embed.color = 0x00ff00

        # Disable all the buttons
        for item in self.children:
            item.disabled = True
        
        # Edit the original message to update the embed and disable the buttons
        await message.edit(embed=original_embed, view=self)
        await interaction.response.send_message("Thank you for your response!", ephemeral=True)
        
        actions = await get_user_field(interaction.user.id, "mod_actions.ban_user")
        if actions is None:
            actions = 0
        setactions = actions + 1
        await update_user_field(interaction.user.id, "mod_actions.ban_user", setactions)
        
        self.stop()



async def create_mod_action(message_channel: discord.Message.channel, message_id: discord.Message.id, role: str, reason: str, ai_response: str):
    # Get the log channel
    log_channel = bot.get_channel(int(settings.LOG_CHANNEL))
    
    # Get the message
    message = await message_channel.fetch_message(message_id)
    
    # Get the role
    if role.lower() == 'moderator':
        role_id = settings.MOD
    elif role.lower() == 'admin':
        role_id = settings.ADMIN
    else:
        return  # Invalid role

    message_content = message.content

    # Create the embed
    embed = Embed(title="Action Required", description=f"<@&{role_id}>, a mod action is required\n{reason}", color=0xff0000)
    embed.add_field(name="AI Response", value=ai_response, inline=False)
    embed.add_field(name="Message", value=message_content, inline=False)
    embed.add_field(name="Channel", value=message_channel.mention, inline=True)
    message_link = f"https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}"
    embed.add_field(name="Message Link", value=f"[Go to message]({message_link})", inline=False)
    embed.add_field(name="Author", value=message.author.mention, inline=True)
    embed.set_footer(text=f"{message_channel.id}:{message_id}")

    # Send the message with the embed and buttons
    view = ModActionService()
    #view.add_item(discord.ui.Button(label='Non-Action', style=discord.ButtonStyle.green))
    await log_channel.send(view=view, embed=embed)
    