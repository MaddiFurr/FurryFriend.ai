from discord.ext import commands
import datetime

class time(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def time(self, ctx):
        async with ctx.channel.typing():
            time = datetime.datetime.now()
            await ctx.send(f"It is {time}!")

async def setup(bot):
    await bot.add_cog(time(bot))