# import modules
import discord
import os
import json
import asyncio
from discord.ext import commands

#load config
with open('./config.json') as f:
  data = json.load(f)
  for c in data['botConfig']:
        print('Online! Ready To Be Controlled')
        print('Prefix: ' + c['prefix'])
        
#define client
bot = commands.Bot(command_prefix = c['prefix'],intents=discord.Intents.all(),status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="Coming Soon!"))
bot.remove_command('help')
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
