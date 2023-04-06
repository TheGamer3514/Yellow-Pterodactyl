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
#bot.remove_command('help')
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
#------------------------------------------Prefix Commands-------------------------------------------------
#--------------------------------Info---------------------------------------
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
#--------------------------------Fun---------------------------------------
#8Ball Command
@bot.command(aliases=['8ball'])
async def magic8ball(ctx):
    await Webhooklogging(c['webhookurl'], f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}8ball")
    embed=discord.Embed(title=":8ball: Magic 8 Ball :8ball:", description=ball8answers[random.randint(0, len(ball8answers)-1)], colour=discord.Colour.random())
    await ctx.send(embed=embed)
#--------------------------------Utility---------------------------------------
#Purge Command
@bot.command(aliases=['useravatar'])
async def avatar(ctx,  member: discord.Member = None):
    if not member:
        member = ctx.author
    await Webhooklogging(c['webhookurl'], f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}avatar {member}")
    embed = discord.Embed(colour=discord.Colour.random(), title=f"{member}'s avatar")
    embed.set_image(url=member.avatar.url)
    await ctx.send(embed=embed)
#--------------------------------Moderation---------------------------------------
#Avatar Command
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
bot.run(c['token'], log_handler=handler, log_level=logging.ERROR)