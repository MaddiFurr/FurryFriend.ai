import discord
from discord import app_commands as apc


class info(apc.Group):
    """Manage general commands"""
    def __init__(self, bot: discord.ext.commands.Bot):
        super().__init__()
        self.bot = bot

    @apc.command()
    async def hello(self, interaction: discord.Interaction):
        """Say "hello" to the bot!"""
        await interaction.response.send_message('Hello {}! Ya cutie!'.format(interaction.user.mention), ephemeral=True)
        print("Hello command ran by {} ({})".format(interaction.user.name,interaction.user.id))

    @apc.command()
    async def version(self, interaction: discord.Interaction):
        """Tells you what version of the bot software is running."""
        await interaction.response.send_message('Bot Running: DEV 0.0.1', ephemeral=True)
        print("Version command ran by {} ({})".format(interaction.user.name,interaction.user.id))