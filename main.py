import discord
from discord.ext import commands
import asyncio
import logging
import os
from utils.config import basicconfig
import datetime

bot = commands.Bot(command_prefix=basicconfig.PREFIX, intents=discord.Intents.all())

async def loadcogs():
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            try:
                await bot.load_extension(f"cogs.{file[:-3]}")
                print(f'[LOGS] Loaded {file}')
            except Exception as e:
                print(f'[ERROR][LOADCOG]{e}')


@bot.event
async def on_event():
    print("Jr Ritz is online!")


asyncio.run(loadcogs())

handler = logging.FileHandler(filename=f"{datetime.date} | {datetime.time}",  mode="w", encoding="utf-8")


bot.run(basicconfig.TOKEN, log_handler=handler)