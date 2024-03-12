import discord
from discord.ext import commands
from discord import app_commands
import datetime

class PurgeCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @app_commands.command()
    @app_commands.checks.has_permissions(manage_messages=True)
    async def purge(self, interaction:discord.Interaction,  amount:int):
        """Purge a specified number of messages from the channel."""

        def calculate_future_time(seconds):
            current_time = datetime.datetime.now()
            future_time = current_time + datetime.timedelta(seconds=seconds)
            return future_time
        
        delete_after = 10

        future_time = calculate_future_time(delete_after)
        await interaction.channel.purge(limit=amount)
        embed = discord.Embed(title="Message Deleted", description=f"**{amount} message(s) deleted by {interaction.user.mention}.**\n\nThis message will be deleted in <t:{future_time.timestamp():.0f}:R>", color=discord.Color.red())
        
        await interaction.response.send_message(embed=embed, delete_after=delete_after)
        # await interaction.response.send_message("Clearing messages", ephemeral=True)

async def setup(bot):
    await bot.add_cog(PurgeCog(bot))