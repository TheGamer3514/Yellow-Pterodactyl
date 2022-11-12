import discord
from discord.ext import commands
class Info(commands.Cog):
    
    def __init__(self, client):
        self.bot = client

    @commands.command()
    async def stats(self, ctx):
        await ctx.send("Servers: 1\nUptime: 99.99%\nBot Made By Gamer3514. Coming Soon!")
    @commands.command(aliases=['botinfo'])
    async def info(self, ctx):
        embed=discord.Embed(title="Bot Info", url="https://github.com/TheGamer3514/Yellow-Pterodactyl", description="**Info:**\n``Bot Creator:`` Gamer3514#7679\n``Support Server:`` [3514](https://discord.gg/WeQ3TpdfZM)", color=0xFCBA03)
        await ctx.send(embed=embed)
    @commands.command(aliases=['bothelp'])
    async def help(self, ctx):
        embed=discord.Embed(title="Bot Help", url="https://github.com/TheGamer3514/Yellow-Pterodactyl", description="**Info:**\n``!help`` - Shows The Help Embed\n``!botinfo`` - Shows The Bot Info\n``!credits`` - Shows The Bot Credits\n``!stats`` - Shows The Bot Stats\n``!update`` - Shows The Bot Update Logs\n**Fun:**\n``!magic8ball`` - Ask the magic 8ball a question or two!\n**Utility:**\n``!avatar`` - Get a user's avatar!", color=0xFCBA03)
        await ctx.send(embed=embed)
    @commands.command(aliases=['botcredits'])
    async def credits(self, ctx):
        embed=discord.Embed(title="Credits", url="https://github.com/TheGamer3514/Yellow-Pterodactyl", description="``Bot Creator:`` Gamer3514#7679\n``Github`` - [Link](https://github.com/TheGamer3514/Yellow-Pterodactyl)\n``Support Server`` - [Link](https://discord.gg/WeQ3TpdfZM)", color=0xFCBA03)
        await ctx.send(embed=embed)
    @commands.command(aliases=['updatelog'])
    async def update(self, ctx):
        embed=discord.Embed(title="Update Logs | v0.0.1", url="https://github.com/TheGamer3514/Yellow-Pterodactyl", description="First Release! Epic!\n**Stuff Added:**\n All the commands\nbot avatar\nAdded To Some Botlists! !botlists to virw them all!", color=0xFCBA03)
        await ctx.send(embed=embed)
async def setup(client):
    await client.add_cog(Info(client))
