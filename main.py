#import modules
import discord
import os
import json
import asyncio
import psutil
from discord_webhook import DiscordWebhook
import random
import multiprocessing
import logging
from discord.ext import commands
ball8answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes - definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']
handler = logging.FileHandler(filename='errors.log', encoding='utf-8', mode='w')
#load config
with open('./config.json') as f:
  data = json.load(f)
  for c in data['botConfig']:
        print('Prefix: ' + c['prefix'])
#Define Bot
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.AutoShardedBot(command_prefix = c['prefix'],intents=intents,status=discord.Status.idle,case_insensitive=True)
bot.remove_command('help')
#------------------------------------------Bot Events-------------------------------------------------
#Auto Updating Status
async def StatusChange():
    while True:
        usercount = len(list(filter(lambda m: m.bot == False, bot.users)))
        await bot.change_presence(activity=discord.Game(f"{c['prefix']}help | {len(bot.guilds)} Servers"))
        await asyncio.sleep(35)
        await bot.change_presence(activity=discord.Game(f"{c['prefix']}help | {usercount} Users"))
        await asyncio.sleep(35)
        await bot.change_presence(activity=discord.Game(f"{c['prefix']}help | discord.gg/3qvpkgWSbF"))
        await asyncio.sleep(35)
        await bot.change_presence(activity=discord.Game(f"{c['prefix']}help | Gamer3514#7679"))
        await asyncio.sleep(35)
#Webhook Logging
async def Webhooklogging(channel,message):
        webhook = DiscordWebhook(url=channel, content=message)
        response = webhook.execute()
        print(message)
#Event that runs when bot is online
@bot.event
async def on_ready():
    print(f'{bot.user} Is Now Online!')
    await bot.loop.create_task(StatusChange())
#------------------------------------------Bot Menus-------------------------------------------------
class HelpDropdown(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label='Info', description='Get a list of info related commands.', emoji='<:info:1071407819670175774>'),
            discord.SelectOption(label='Fun', description='Get a list of fun related commands.', emoji='<:awesome:1093813270802075728>'),
            discord.SelectOption(label='Utility', description='Get a list of utility related commands.', emoji='<a:arrow:942025249908752395>'),
            discord.SelectOption(label='Moderation', description='Get a list of moderation related commands.', emoji='<:maintenace:926794294017286165>'),
        ]
        super().__init__(placeholder='Choose Command Category', min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Info":
            embed=discord.Embed(title="Yellow Pterodactyl - Info Commands", colour=discord.Colour.random())
            embed.add_field(name=f"{c['prefix']}help",value="View this help menu.",inline=False)
            embed.add_field(name=f"{c['prefix']}stats",value="View bot stats.",inline=False)
            embed.add_field(name=f"{c['prefix']}ping",value="Get bot ping.",inline=False)
            embed.add_field(name=f"{c['prefix']}vote",value="Vote for me on top.gg!",inline=False)
            embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/4zTjIjkHc-SZduIGBSaA9mZFtMYawoVozGtzdoZUHm0/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1037361246464393216/f068ac884e61133caaa896a4a52e51cc.png")
            await interaction.response.edit_message(embed=embed)
        elif self.values[0] == "Fun":
            embed=discord.Embed(title="Yellow Pterodactyl - Fun Commands", colour=discord.Colour.random())
            embed.add_field(name=f"{c['prefix']}8ball",value="Use a magic 8 ball.",inline=False)
            embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/4zTjIjkHc-SZduIGBSaA9mZFtMYawoVozGtzdoZUHm0/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1037361246464393216/f068ac884e61133caaa896a4a52e51cc.png")
            await interaction.response.edit_message(embed=embed)
        elif self.values[0] == "Utility":
            embed=discord.Embed(title="Yellow Pterodactyl - Utility Commands", colour=discord.Colour.random())
            embed.add_field(name=f"{c['prefix']}avatar",value="Grab someone's avatar.",inline=False)
            embed.add_field(name=f"{c['prefix']}serverinfo",value="Get info on the current server.",inline=False)
            embed.add_field(name=f"{c['prefix']}userinfo",value="Get info on a user.",inline=False)
            embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/4zTjIjkHc-SZduIGBSaA9mZFtMYawoVozGtzdoZUHm0/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1037361246464393216/f068ac884e61133caaa896a4a52e51cc.png")
            await interaction.response.edit_message(embed=embed)
        elif self.values[0] == "Moderation":
            embed=discord.Embed(title="Yellow Pterodactyl - Moderation Commands", colour=discord.Colour.random())
            embed.add_field(name=f"{c['prefix']}purge",value="Purge an amount of messages.",inline=False)
            embed.add_field(name=f"{c['prefix']}ban",value="Ban a user from your server.",inline=False)
            embed.add_field(name=f"{c['prefix']}unban",value="Unban a user from your server",inline=False)
            embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/4zTjIjkHc-SZduIGBSaA9mZFtMYawoVozGtzdoZUHm0/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1037361246464393216/f068ac884e61133caaa896a4a52e51cc.png")
            await interaction.response.edit_message(embed=embed)
        else:
            embed=discord.Embed(title="Yellow Pterodactyl - Error!", description="Somehow you selected a choice i did not know was there!",colour=discord.Colour.red())
            embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/4zTjIjkHc-SZduIGBSaA9mZFtMYawoVozGtzdoZUHm0/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1037361246464393216/f068ac884e61133caaa896a4a52e51cc.png")
            await interaction.response.edit_message(embed=embed)


class HelpDropdownView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(HelpDropdown())
#------------------------------------------Prefix Commands-------------------------------------------------
#--------------------------------Info---------------------------------------
#Help Command
@bot.command(aliases=['bothelp'])
async def help(ctx):
    await Webhooklogging(c['webhookurl'], f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}help")
    embed=discord.Embed(title="Yellow Pterodactyl", description="Version 2.0", colour=discord.Colour.random())
    view = HelpDropdownView()
    await ctx.send(view=view,embed=embed)
#Stats Command
@bot.command(name='stats', aliases=['botstats'])
async def stats(ctx):
    usercount = len(list(filter(lambda m: m.bot == False, bot.users)))
    await Webhooklogging(c['webhookurl'], f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}stats")
    embed = discord.Embed(
        title = f'My Stats:',
        colour=discord.Colour.random())
    embed.add_field(name="Bot Owner", value="<@763471049894527006> (763471049894527006) Gamer3514#7679", inline=False)
    embed.add_field(name="Cpu Cores", value=multiprocessing.cpu_count(), inline=False)
    embed.add_field(name="Server Count", value=f"{len(bot.guilds)}", inline=False)
    embed.add_field(name="User Count", value=f"{usercount}", inline=False)
    embed.add_field(name="Bot Latency", value=f"{round(bot.latency * 1000)}ms", inline=False)
    embed.add_field(name="Cpu Usage", value=f"{psutil.cpu_percent()}%", inline=False)
    embed.add_field(name="Memory Usage", value=f"{psutil.virtual_memory().percent}%", inline=False)
    embed.add_field(name="Total Memory", value=f"{round(psutil.virtual_memory().total / (1024.0 **3))} GB", inline=False)
    await ctx.send(embed=embed)
@bot.command(aliases=['botping'])
async def ping(ctx):
    await Webhooklogging(c['webhookurl'], f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}ping")
    embed = discord.Embed(title="Pong!", description=f"{round(bot.latency * 1000)}ms", colour=discord.Colour.random())
    await ctx.send(embed=embed)
@bot.command(aliases=['votebot'])
async def vote(ctx):
    await Webhooklogging(c['webhookurl'], f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}ping")
    embed = discord.Embed(description=" [Vote Here!](https://top.gg/bot/1037361246464393216/vote)", colour=discord.Colour.random())
    await ctx.send(embed=embed)
#--------------------------------Fun---------------------------------------
#8Ball Command
@bot.command(aliases=['8ball'])
async def magic8ball(ctx):
    await Webhooklogging(c['webhookurl'], f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}8ball")
    embed=discord.Embed(title=":8ball: Magic 8 Ball :8ball:", description=ball8answers[random.randint(0, len(ball8answers)-1)], colour=discord.Colour.random())
    await ctx.send(embed=embed)
#--------------------------------Utility---------------------------------------
#Server Info Command
@bot.command(aliases=['guildinfo'])  
async def serverinfo(ctx):
    await Webhooklogging(c['webhookurl'], f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}serverinfo")
    role_count = len(ctx.guild.roles)
    emoji_count = len(ctx.guild.emojis)
    list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]
    embed = discord.Embed(title=f"Server Info - {ctx.guild.name}", description="Server Information", color=discord.Color.random())
    embed.add_field(name="Server ID", value=ctx.guild.id, inline=False)
    embed.add_field(name="Server Owner", value=ctx.guild.owner, inline=False)
    embed.add_field(name="Verification Level", value=ctx.guild.verification_level, inline=False)
    embed.add_field(name="Total Members", value=ctx.guild.member_count, inline=False)
    embed.add_field(name="Total Bots", value=len(list_of_bots), inline=False)
    embed.add_field(name="Total Text Channels", value=len(ctx.guild.text_channels), inline=False)
    embed.add_field(name="Total Voice Channels", value=len(ctx.guild.voice_channels), inline=False)
    embed.add_field(name="Total Categories", value=len(ctx.guild.categories), inline=False)
    embed.add_field(name="Total Roles", value=role_count, inline=False)
    embed.add_field(name="Total Emojis", value=emoji_count, inline=False)
    embed.add_field(name="Created At", value=ctx.guild.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
    await ctx.send(embed=embed)
#Userinfo Command
@bot.command(aliases=['infouser'])
async def userinfo(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author
    await Webhooklogging(c['webhookurl'], f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}userinfo {member}")
    embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
    embed.set_author(name=f"User Info - {member}")
    embed.set_footer(text=f"Requested by {ctx.author}")
    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Guild Name:", value=member.display_name)
    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Top Role:", value=member.top_role.mention)
    embed.add_field(name="Bot?", value=member.bot)
    await ctx.send(embed=embed)
#Avatar Command
@bot.command(aliases=['useravatar'])
async def avatar(ctx,  member: discord.Member = None):
    if not member:
        member = ctx.author
    await Webhooklogging(c['webhookurl'], f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}avatar {member}")
    embed = discord.Embed(colour=discord.Colour.random(), title=f"{member}'s avatar")
    embed.set_image(url=member.avatar.url)
    await ctx.send(embed=embed)
#--------------------------------Moderation---------------------------------------
#Purge Command
@bot.command(aliases=['purgemessages'])
async def purge(ctx, amount: int = None):
    await Webhooklogging(c['webhookurl'], f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}purge {amount}")
    if not amount:
        embed = discord.Embed(colour=discord.Colour.red(), title=f"No Purge Amount Given!\nCorrect Usage: {c['prefix']}purge [amount]")
    try:
        embed = discord.Embed(colour=discord.Colour.random(), title=f"Purged {amount} Messages!")
        await ctx.channel.purge(limit=amount)
    except:
        embed = discord.Embed(colour=discord.Colour.red(), title=f"Failed to purge {amount} messages.\nThis could be due to the messages being older than 14 days or because i am missing ``manage messages`` permission.")
    message = await ctx.send(embed=embed)
    await asyncio.sleep(5)
    message.delete
#Ban Command
@bot.command(aliases=['banuser'])
async def ban(ctx, member : discord.Member, *, reason = None):
    await Webhooklogging(c['webhookurl'], f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}ban {member} {reason}")
    if ctx.author.guild_permissions.ban_members:
        try:
            await member.ban(reason=reason)
            embed = discord.Embed(colour=discord.Colour.blurple(), title="Banned!", description=f"{member} was banned by {ctx.author}!\nReason: {reason}")
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(colour=discord.Colour.red(), title="Error!", description=f"I do not have enough permissions to ban {member} / they have a higher role than me.")
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(colour=discord.Colour.red(), title="Error!", description=f"You do not have enough permissions to ban {member}")
        await ctx.send(embed=embed)

#Unban Command
@bot.command(aliases=['unbanuser'])
async def unban(ctx, *, member):
    await Webhooklogging(c['webhookurl'], f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}unban {member}")
    if ctx.author.guild_permissions.ban_members:
        banned_users = ctx.guild.bans()
        member_name, member_discriminator = member.split("#")
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(colour=discord.Colour.blurple(), title="Unbanned!", description=f"{member} has been unbanned by {ctx.author}")
                await ctx.send(embed=embed)
                return
    else:
        embed = discord.Embed(colour=discord.Colour.red(), title="Error!", description=f"You do not have enough permissions to ban {member}")
        await ctx.send(embed=embed)
bot.run(c['token'], log_handler=handler, log_level=logging.ERROR)