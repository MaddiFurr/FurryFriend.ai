import discord
from ...services.BotService import bot
from ...services.SettingsService import settings
from ...services.LoggingService import log
from ...services.DBService import add_new_user
import time

@bot.event
async def on_member_join(member):
    epoch = int(time.time())
    
    # When a member joins the server, inform the logging channel
    e = discord.Embed(title="User Joined", description=f"A user has joined the server {member.name}", color=0x979c9f)
    e.add_field(name="Action Severity", value="1 - Low", inline=False)
    e.add_field(name="User", value=member.mention, inline=True)
    e.add_field(name="Account Created", value="<t:{}>".format(str(int(member.created_at.timestamp()))), inline=True)
    e.add_field(name="Total Members", value=member.guild.member_count, inline=True)
    e.add_field(name="Occurred at", value="<t:{}>".format(str(epoch)), inline=False)
    e.set_image(url=member.display_avatar)
    await log(e, f"User Joined {member.name} ({member.id})", None, None, None)

    # Assign the auto role to the member
    auto_role = member.guild.get_role(int(settings.AUTO_ROLE))
    if auto_role is not None:
        await member.add_roles(auto_role)
        print(f"Role {auto_role.name} assigned to {member.name}")
    else:
        print(f"Role with ID {settings.AUTO_ROLE} not found")
    
    # Add the user to the database
    await add_new_user(member.id, member.name, member.nick, member.created_at, member.joined_at)
    

    
    
