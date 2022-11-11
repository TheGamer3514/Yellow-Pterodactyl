import discord
import random
from discord.ext import commands
answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']
class Utility(commands.Cog):
    
    def __init__(self, client):
        self.bot = client

    @commands.command()
    async def avatar(self, ctx,  member: discord.Member = None):
        if not member:
            embed=discord.Embed(title="No User Selected", description="Correct Usage:\n!avatar @user\n!avatar userid", color=0xFCBA03)
            await ctx.send(embed=embed)
        embed = discord.Embed(colour=discord.Colour.random(), title=f"{member}'s avatar")
        embed.set_image(url=member.avatar.url)
        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(Utility(client))
    
    
