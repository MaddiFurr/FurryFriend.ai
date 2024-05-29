import discord
from .BotService import bot
from .SettingsService import settings
from .DBService import write_user_data
from .DBService import write_server_data
from .DBService import increment_user_action
from .DBService import update_username
from .DBService import increment_channel_action
from .DBService import update_channel_name
import os
import time


async def log(message: discord.Embed = None, logfile: str = None, command: str = None, user: discord.user = None, channel: discord.channel = None, number: int = 1):
    # Don't log if the user is a bot
    if command == "on_message" and user.bot:
        return
    
    if message is not None:
        loggingchannel = bot.get_channel(int(settings.LOG_CHANNEL))
        await loggingchannel.send(embed=message)
    
    if logfile is not None:
        # Get the current date and time
        current_time = time.localtime()

        # Create the log file name
        log_file_name = time.strftime("%Y%m%d-log.log", current_time)

        # Create the log file path
        log_file_path = os.path.join('configs', 'logs', log_file_name)

        # Check if the log directory exists, if not, create it
        if not os.path.exists(os.path.dirname(log_file_path)):
            os.makedirs(os.path.dirname(log_file_path))

        # Check if the log file exists, if not, create it
        if not os.path.exists(log_file_path):
            open(log_file_path, 'w').close()

        # Append the logfile variable to the log file
        with open(log_file_path, 'a') as f:
            # Add the current time to the logfile variable
            log_entry = time.strftime("[%H:%M:%S]: ", current_time) + logfile
            f.write(log_entry + "\n")
        
        print(log_entry)
    
    
    
    if command is not None:
        #await increment_user_action(user, command, channel, number)
        if user.nick is None:
            nick = None
        else:
            nick = user.nick
        await update_username(user.id, user.name, nick)
        if channel is not None:
            await update_channel_name(channel.id, channel.name)
            await increment_channel_action(channel, command, user, number)