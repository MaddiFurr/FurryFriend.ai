import discord
from discord import app_commands as apc
from ...services.BotService import bot
import configparser
import os

async def update_logchannel(interaction: discord.Interaction, user: discord.User, channel: discord.TextChannel):
        """Change the guild's log channel"""
        
        # Get the absolute path of the directory of the current script
        dir_path = os.path.dirname(os.path.realpath(__file__))

        # Construct the path to the bot.conf file
        conf_path = os.path.join(dir_path, '../../../bot.conf')
        print(conf_path)
        config = configparser.ConfigParser()
        
        config = configparser.ConfigParser()
        
        config.set('Bot', 'LOGCHANNEL', str(channel.id))
        with open(conf_path, 'w') as configfile:
            config.write(configfile)

        await interaction.response.send_message("Changed the log channel to #{}".format(channel), ephemeral=True)
        print("Log Channel command ran by {} ({}). Changed log channel to: {}".format(user.name,user.id, channel))