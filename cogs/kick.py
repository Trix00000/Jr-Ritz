import discord
from discord import app_commands, ui
from discord.ext import commands


class KickCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name="kick", description="kicks a user")
    @app_commands.checks.has_permissions(kick_members=True)
    async def kick(self, interaction, user:discord.Member, reason: str="No reason provided"):
        try:
            server_name = interaction.guild.name
            await user.kick(reason=reason)
            embed = discord.Embed(title="Kicked!",
                                description=f"✅ Successfully kicked {user.mention}",
                                color=discord.Color.red())
            await interaction.response.send_message(embed=embed, ephemeral=True)
            await user.send(f"You have been kicked from from {server_name}, for the reason, '{reason}'")
        except Exception as e:
            try:
                await interaction.response.send_message(e, ephemeral=True)
            except discord.InteractionResponded:
                pass
            
            
async def setup(bot):
    await bot.add_cog(KickCog(bot))