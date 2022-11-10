import discord
from discord.ext import commands
class Info(commands.Cog):
    
    def __init__(self, client):
        self.bot = client

    @commands.command()
    async def stats(self, ctx):
        await ctx.send("Servers: 1\nUptime: 99.99%\nBot Made By Gamer3514. Coming Soon!")
    @commands.command()
    async def info(self, ctx):
        embed=discord.Embed(title="Bot Info", url="https://github.com/TheGamer3514/Yellow-Pterodactyl", description="**Info:**\n``Bot Creator:`` Gamer3514#7679\n``Host:`` [Huguitis Nodes](https://discord.gg/byarHVDznN)\n``Support Server:`` [3514](https://discord.gg/WeQ3TpdfZM)", color=0xFCBA03)
        await ctx.send(embed=embed)
    @commands.command()
    async def botinfo(self, ctx):
        embed=discord.Embed(title="Bot Info", url="https://github.com/TheGamer3514/Yellow-Pterodactyl", description="**Info:**\n``Bot Creator:`` Gamer3514#7679\n``Host:`` [Huguitis Nodes](https://discord.gg/byarHVDznN)\n``Support Server:`` [3514](https://discord.gg/WeQ3TpdfZM)", color=0xFCBA03)
        await ctx.send(embed=embed)
    @commands.command()
    async def help(self, ctx):
        embed=discord.Embed(title="Bot Help", url="https://github.com/TheGamer3514/Yellow-Pterodactyl", description="**Info:**\n``!help`` - Shows The Help Embed\n``!botinfo`` - Shows The Bot Info\n``!stats`` - Shows The Bot Stats", color=0xFCBA03)
        await ctx.send(embed=embed)
async def setup(client):
    await client.add_cog(Info(client))
