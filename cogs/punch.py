import discord
from discord.ext import commands
from discord import app_commands
import praw
import random


# Reddit API credentials
REDDIT_CLIENT_ID = 'awdawdeawd'
REDDIT_CLIENT_SECRET = 'adawdawd'
REDDIT_USER_AGENT = 'dawdawdadawd'

# Subreddit to fetch memes from
SUBREDDIT_NAME = 'nadawda'



class PunchCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="punch")
    async def punch(self, ctx: commands.Context, user: discord.Member):
        
        titles_list = []
        gif_list = []

        with open("files/punch_text.txt", "r") as f:
            for line in f:
                titles_list.append(line.strip())

        with open("files/punch_gif.txt", "r") as f:
            for line in f:
                gif_list.append(line.strip())

        title = random.choice(titles_list)
        gif = random.choice(gif_list)

        embed = discord.Embed(title=title, color=discord.Color.random())
        embed.set_image(url=gif)
        await ctx.reply(embed=embed)
        
        

        
            
            
            
async def setup(bot):
    await bot.add_cog(PunchCog(bot))   
    