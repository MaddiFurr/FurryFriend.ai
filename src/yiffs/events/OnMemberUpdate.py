import discord
from ...services.BotService import bot
from ...services.SettingsService import settings
import time

@bot.event
async def on_member_update(before, after):
    epoch = int(time.time())
    
    # Check if the user's nickname have changed
    if before.nick != after.nick:
        e = discord.Embed(title="User Nickname Updated", description=f"A guild member's nickname has been updated {before.name}", color=0x979c9f)
        e.add_field(name="Action Severity", value="1 - Low", inline=False)
        e.add_field(name="User", value=before.mention, inline=False)
        e.add_field(name="Nickname Before", value=before.display_name, inline=True)
        e.add_field(name="Nickname After", value=after.display_name, inline=True)
        e.add_field(name="Occurred at", value="<t:{}>".format(str(epoch)), inline=False)
        loggingchannel = bot.get_channel(int(settings.LOG_CHANNEL))
        await loggingchannel.send(embed=e)
        print("User Nickname Updated {} - > {}".format(before.name, after.name))

        return
    
    # Check if the user's roles have changed
    if before.roles != after.roles:
        # Extract role names
        before_roles = ', '.join([role.name for role in before.roles])
        after_roles = ', '.join([role.name for role in after.roles])

        e = discord.Embed(title="User Roles Updated", description=f"A guild member's roles have been updated {before.name}", color=0x979c9f)
        e.add_field(name="Action Severity", value="1 - Low", inline=False)
        e.add_field(name="User", value=before.mention, inline=False)
        e.add_field(name="Roles Before", value=before_roles, inline=True)  # Use role names
        e.add_field(name="Roles After", value=after_roles, inline=True)  # Use role names
        e.add_field(name="Occurred at", value="<t:{}>".format(str(epoch)), inline=False)
        loggingchannel = bot.get_channel(int(settings.LOG_CHANNEL))
        await loggingchannel.send(embed=e)
        print("User Roles Updated {} - > {}".format(before_roles, after_roles))

        return
