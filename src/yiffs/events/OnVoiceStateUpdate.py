import discord
from ...services.BotService import bot
from ...services.SettingsService import settings
from ...services.LoggingService import log
from datetime import datetime

# Dictionary to store the join times of members
join_times = {}

@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        # The member has joined a voice channel
        join_times[member.id] = datetime.now()
        await log(None, f"{member.name} has joined the voice channel {after.channel.name} ({after.channel.id})", None, None, None, None)
    elif before.channel is not None and (after.channel is None or before.channel != after.channel):
        # The member has left a voice channel or moved to another channel
        join_time = join_times.pop(member.id, None)
        if join_time is not None:
            duration = datetime.now() - join_time
            total_seconds = int(duration.total_seconds())
            hours = total_seconds // 3600
            minutes = (total_seconds // 60) % 60
            seconds = total_seconds % 60
            await log(None, f"{member.name} has left the voice channel {before.channel.name} ({before.channel.id}) after {hours}h:{minutes}m:{seconds}s", "Total Voice Time", member, before.channel, duration.total_seconds())