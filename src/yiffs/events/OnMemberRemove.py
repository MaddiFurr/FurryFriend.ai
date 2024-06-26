import discord
from ...services.BotService import bot
from ...services.SettingsService import settings
from ...services.LoggingService import log
import time

@bot.event
async def on_member_remove(member):
    epoch = int(time.time())
    
    # When a member joins the server, inform the logging channel
    e = discord.Embed(title="User Left", description=f"A user has left the server {member.name}", color=0x979c9f)
    e.add_field(name="Action Severity", value="1 - Low", inline=False)
    e.add_field(name="User", value=member.mention, inline=True)
    e.add_field(name="Account Created", value="<t:{}>".format(str(int(member.created_at.timestamp()))), inline=True)
    e.add_field(name="Total Members", value=member.guild.member_count, inline=True)
    e.add_field(name="Occurred at", value="<t:{}>".format(str(epoch)), inline=False)
    e.set_image(url=member.display_avatar)
    await log(e, f"User Left {member.name} ({member.id})", None, None, None)
    
