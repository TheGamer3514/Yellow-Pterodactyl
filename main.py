# import modules
import discord
import os
import json
import asyncio
from discord.ext import commands
#logging
import logging

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

#load config
with open('./config.json') as f:
  data = json.load(f)
  for c in data['botConfig']:
        print('Online! Ready To Be Controlled')
        print('Prefix: ' + c['prefix'])
#define client
bot = commands.Bot(command_prefix = c['prefix'],intents=discord.Intents.all(),status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="Coming Soon!"))
bot.remove_command('help')
#on guild join
@bot.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            embed = discord.Embed(title="Yellow Pterodactyl", description="<a:arrow:942025249908752395>Hello. Thank you for inviting me to your server! Get started by running ``!help``!", color=(65535))
            embed.add_field(name="<:no:942044962541936671> WARNING <:no:942044962541936671>", value='<a:arrow:942025249908752395>This bot is still in active development! Downtime May Occur Often!', inline=False)
            await channel.send(embed=embed)
        break
#start bot
async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
 #start bot
async def main():
    async with bot:
        await load()
        await bot.start(c['token'])
asyncio.run(main())
