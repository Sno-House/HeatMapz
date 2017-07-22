import discord
from discord.ext import commands

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def punch(self, user : discord.Member):
        """I will kill you!"""

        #Your code will go here
        await self.bot.say("A believing heart is magic " + user.mention + "!")

def setup(bot):
    bot.add_cog(Mycog(bot))
