import discord
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """Welcome new members"""
        channel = member.guild.system_channel
        if channel:
            await channel.send(f'Welcome {member.mention} to the server!')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """Handle command errors"""
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Command not found!")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to use this command!")

async def setup(bot):
    await bot.add_cog(Events(bot))