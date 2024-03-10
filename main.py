import discord
from discord.ext import commands
import asyncio
import logging
import os
from utils.config import basicconfig
import datetime

bot = commands.Bot(command_prefix=basicconfig.PREFIX, intents=discord.Intents.all())
bot.help_command = None
async def loadcogs():
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            try:
                await bot.load_extension(f"cogs.{file[:-3]}")
                print(f'[LOGS] Loaded {file}')
            except Exception as e:
                print(f'[ERROR][LOADCOG]{e}')


@bot.event
async def on_ready():
    slash_commands = await bot.tree.sync()
    print("----------------------------=--------------------------")
    print("Jr Ritz is online!")
    print(f"Synced commands = {len(slash_commands)}")
    print("----------------------------=--------------------------")


asyncio.run(loadcogs())

handler = logging.FileHandler(filename=f"error.log",  mode="w", encoding="utf-8")


bot.run(basicconfig.TOKEN, log_handler=handler)