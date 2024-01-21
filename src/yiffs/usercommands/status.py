import discord
from discord import app_commands as apc
from ...services.PermissionChecker import permission_checker


async def status(interaction: discord.Interaction, user: discord.User):
        """Get a user's status and activities"""
        if await permission_checker(interaction.user, 'mod') == False:
            await interaction.response.send_message("You don't have permission to run this command!", ephemeral=True)
            return
        
        user = user or interaction.user
        guild = interaction.guild
        member = guild.get_member(user.id)

        # Fetch user status
        status = str(member.status)

        # Fetch user activities
        # Fetch user activities
        # Fetch user activities
        activities = '\n---\n'.join([f"{activity.type.name}: {activity.name}" if isinstance(activity, discord.Spotify) else f"{activity.type.name}: {activity.name}, URL: {activity.url or 'No URL'}" for activity in member.activities])

        # Create an embed message
        e = discord.Embed(title=f"{member.display_name}'s Status and Activities", description=None, color=member.accent_color)
        e.add_field(name='Status', value=status)
        e.add_field(name='Activities', value=activities or 'No activities')

        # Check if the user is listening to Spotify
        for activity in member.activities:
            if isinstance(activity, discord.Spotify):
                spotify = activity
                e.add_field(name='Listening to', value=spotify.title, inline=False)
                e.add_field(name='Track Link', value=spotify.track_url, inline=False)
                e.add_field(name='Artist', value=', '.join(spotify.artists), inline=False)
                e.add_field(name='Album', value=spotify.album, inline=False)
                e.add_field(name='Started Listening', value=spotify.created_at.strftime("%H:%M:%S"), inline=False)
                e.add_field(name='Duration', value=str(int(spotify.duration)), inline=False)
                e.set_image(url=spotify.album_cover_url)
                break

        await interaction.response.send_message(embed=e, ephemeral=False)
        print("Status command ran by {} ({}) on user {} ({})".format(interaction.user.name,interaction.user.id,member.name,member.id))