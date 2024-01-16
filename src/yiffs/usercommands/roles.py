import discord
from discord import app_commands as apc
from ...services.PermissionChecker import permission_checker

async def roles(interaction: discord.Interaction, user: discord.User):
        """Get a user's roles"""
        user = user or interaction.user
        guild = interaction.guild
        member = guild.get_member(user.id)

        # Get the member's roles
        roles = member.roles

        # Get the names of the roles, excluding the @everyone role
        role_names = [role.name for role in roles if role.name != "@everyone"]

        # Create an embed to display the user's status and roles
        e = discord.Embed(title=f"{user.display_name}'s status", description="Here are the user's roles!", color=user.accent_color)

        # Add the user's roles to the embed
        e.add_field(name="Roles", value=", ".join(role_names))

        await interaction.response.send_message("Here is <@{}>'s roles!".format(user.id), embed=e, ephemeral=True)

        print("Roles command ran by {} ({}) on user {} ({})".format(interaction.user.name,interaction.user.id,member.name,member.id))