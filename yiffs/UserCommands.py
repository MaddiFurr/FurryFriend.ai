import discord
from discord import app_commands as apc

class user(apc.Group):
    """Manage general commands"""
    def __init__(self, bot: discord.ext.commands.Bot):
        super().__init__()
        self.bot = bot
    
    
    @apc.command()
    async def status(self, interaction: discord.Interaction, user: discord.User = None):
        user = user or interaction.user
        guild = interaction.guild
        member = guild.get_member(user.id)

        # Fetch user status
        status = str(member.status)

        # Fetch user activities
        activities = '\n---\n'.join([str(activity) for activity in member.activities])

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
                e.add_field(name='Duration', value=str(spotify.duration), inline=False)
                e.set_image(url=spotify.album_cover_url)
                break

        await interaction.response.send_message(embed=e, ephemeral=False)

    @apc.command()
    async def account(self, interaction: discord.Interaction, user: discord.User):
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