from discord.ext import commands

class hello(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        async with ctx.channel.typing():
            author = ctx.author
            await ctx.send(f"Hewwo {author.mention} :3")

async def setup(bot):
    await bot.add_cog(hello(bot))