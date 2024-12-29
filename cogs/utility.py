import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Kick a member from the server"""
        await member.kick(reason=reason)
        await ctx.send(f'{member.name} has been kicked.')

    @commands.command(name='clear')
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        """Clear specified number of messages"""
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f'{amount} messages cleared.', delete_after=5)

async def setup(bot):
    await bot.add_cog(Moderation(bot))