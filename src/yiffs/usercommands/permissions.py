import discord
from discord import app_commands as apc
from ...services.PermissionChecker import permission_checker

async def permissions(interaction: discord.Interaction, user: discord.User):
        """Get a user's permissions"""
        if await permission_checker(interaction.user, 'admin') == False:
            await interaction.response.send_message("You don't have permission to run this command!", ephemeral=True)
            return
        
        user = user or interaction.user
        guild = interaction.guild
        member = guild.get_member(user.id)

        # Define the permissions you want to check for
        permissions_to_check = ['administrator', 'ban_members', 'change_nickname', 'create_events',
                                'create_expressions', 'create_instant_invite' 'create_private_threads', 'create_public_threads',
                                'deafen_members', 'kick_members', 'manage_channels', 'manage_emojis',
                                'manage_emojis_and_stickers', 'manage_events', 'manage_expressions',
                                'manage_guild', 'manage_messages', 'manage_nicknames', 'manage_permissions',
                                'manage_roles', 'manage_threads', 'manage_webhooks', 'mention_everyone',
                                'moderate_members', 'move_members', 'mute_members', 'view_audit_log',
                                'view_guild_insights']

        # Get the member's permissions
        permissions = member.guild_permissions

        # Convert permissions to a dictionary
        permissions_dict = {perm[0]: perm[1] for perm in iter(permissions)}

        # Create an embed to display the permissions
        e = discord.Embed(title=f"{user.display_name}'s permissions", description="Here are the permissions!", color=user.accent_color)

        # Check each permission and add it to the embed
        for permission in permissions_to_check:
            if permission in permissions_dict:
                e.add_field(name=permission, value=str(permissions_dict[permission]))

        await interaction.response.send_message("Here are <@{}>'s permissions!".format(user.id), embed=e, ephemeral=True)

        print("Permissions command ran by {} ({}) on user {} ({})".format(interaction.user.name,interaction.user.id,member.name,member.id))