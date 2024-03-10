import discord
from discord.ext import commands
from discord import app_commands

class UnbanCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='unban', description=f"Unbans a user from the server.")
    async def unban(self, interaction: discord.Interaction, user_id:int, reason:str=None):
        # Check if the user has the necessary permissions to unban members
        if interaction.author.guild_permissions.ban_members:
            # Attempt to unban the user
            try:
                # Fetch the ban entry for the specified user
                ban_entry = await interaction.guild.fetch_ban(discord.Object(id=user_id))
                
                # Unban the user
                await interaction.guild.unban(ban_entry.user, reason=reason)
                await interaction.response.send_message(f'{ban_entry.user.name}#{ban_entry.user.discriminator} has been unbanned from the server. Reason: {reason}')
            except discord.NotFound:
                await interaction.response.send_message(f'User with ID {user_id} is not banned.')
            except discord.Forbidden:
                await interaction.response.send_message("I don't have the necessary permissions to unban members.")
        else:
            await interaction.response.send_message("You don't have the necessary permissions to unban members.")


async def setup(bot):
    await bot.add_cog(UnbanCog(bot))
