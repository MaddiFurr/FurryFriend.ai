import discord
from discord import app_commands as apc
from ...services.PermissionChecker import permission_checker

async def account(interaction: discord.Interaction, user: discord.User):
        """Get a user's account information"""
        if await permission_checker(interaction.user, 'mod') == False:
            await interaction.response.send_message("You don't have permission to run this command!", ephemeral=True)
            return
        
        user = user or interaction.user
        guild = interaction.guild
        member = guild.get_member(user.id)
        
        # Fetch user status
        status = str(member.status)
        
        e = discord.Embed(title=user.display_name+"'s info", description="Heres what I could find!", color=user.accent_color)
        e.add_field(name='Title', value=user.name)
        e.add_field(name='User ID', value=user.id)
        e.add_field(name='Status', value=status)
        e.add_field(name='Highest Role', value=user.top_role)
        e.add_field(name='Join Date', value=user.joined_at)
        e.add_field(name='Registration Date', value=user.created_at)
        e.add_field(name='Profile Picture', value=user.avatar)
        e.set_image(url=str(user.avatar))
        await interaction.response.send_message("Heres is <@{}>'s info!".format(user.id), embed=e, ephemeral=False)
        print("Account command ran by {} ({}) on user {} ({})".format(interaction.user.name,interaction.user.id,member.name,member.id))