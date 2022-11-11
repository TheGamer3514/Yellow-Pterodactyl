import discord
import random
from discord.ext import commands
answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']
class Fun(commands.Cog):
    
    def __init__(self, client):
        self.bot = client

    @commands.command(aliases=['8ball'])
    async def magic8ball(self, ctx):
        embed=discord.Embed(title=":8ball: Magic 8 Ball :8ball:", description=answers[random.randint(0, len(answers)-1)], color=0xFCBA03)
        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(Fun(client))
    
    
  
