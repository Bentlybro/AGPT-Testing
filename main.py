import discord
from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping')
    async def ping(self, ctx):
        """Check the bot's latency"""
        latency = round(self.bot.latency * 1000)
        await ctx.send(f'Pong! Latency: {latency}ms')

    @commands.command(name='info')
    async def info(self, ctx):
        """Display bot information"""
        embed = discord.Embed(title="Bot Information", color=discord.Color.blue())
        embed.add_field(name="Name", value=self.bot.user.name)
        embed.add_field(name="Servers", value=len(self.bot.guilds))
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Utility(bot))