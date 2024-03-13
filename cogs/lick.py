import discord
from discord.ext import commands
from discord import app_commands
import praw
import random


class lickCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="lick")
    async def lick(self, ctx: commands.Context, user: discord.Member):
        
        if ctx.author == user:

            dumb_titles_list = []

            with open("files/lick_dumb.txt", "r") as f:
                for line in f:
                    dumb_titles_list.append(line.strip())
            embed = discord.Embed(title=random.choice(dumb_titles_list), color=discord.Color.random())
            await ctx.send(embed=embed)



        else:
            titles_list = []
            gif_list = []

            with open("files/lick_text.txt", "r") as f:
                for line in f:
                    titles_list.append(line.strip())

            with open("files/lick_gif.txt", "r") as f:
                for line in f:
                    gif_list.append(line.strip())

            title = random.choice(titles_list)
            gif = random.choice(gif_list)
            formated_title = title.replace("[User]", user.mention).replace("[Author]", ctx.author.mention)
            embed = discord.Embed(title="", description=f"**{formated_title}**", color=discord.Color.random())
            embed.set_image(url=gif)
            await ctx.reply(embed=embed)
        
        

        
            
            
            
async def setup(bot):
    await bot.add_cog(lickCog(bot))   
    