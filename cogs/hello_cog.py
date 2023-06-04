from discord.ext import commands

class HelloCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.content.lower() == 'hello':
            await message.channel.send(f'Hello {message.author.mention}!')

def setup(bot):
    bot.add_cog(HelloCog(bot))