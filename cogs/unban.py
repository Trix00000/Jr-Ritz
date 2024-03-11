import discord
from discord.ext import commands
from discord import app_commands

class UnbanCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='unban', description=f"Unbans a user from the server.")
    @app_commands.checks.has_permissions(ban_members=True)
    async def unban(self, interaction: discord.Interaction, user_id:str, reason:str=None):
            # Attempt to unban the user
            
            try:
                user_id = int(user_id)
                # Fetch the ban entry for the specified user
                ban_entry = await interaction.guild.fetch_ban(discord.Object(id=user_id))
                
                # Unban the user
                await interaction.guild.unban(ban_entry.user, reason=reason)
                await interaction.response.send_message(f'{ban_entry.user.name}#{ban_entry.user.discriminator} has been unbanned from the server. Reason: {reason}')
            except discord.NotFound:
                await interaction.response.send_message(f'User <@{user_id}> ({user_id}) is not banned.')
            except discord.Forbidden:
                await interaction.response.send_message("I don't have the necessary permissions to unban members.")
            except ValueError:
                 await interaction.response.send_message("Please provide a valid user id! (For example: 1142763665775415763)", ephemeral=True)
            except Exception as e:
                 await interaction.response.send_message(f"An error occured: {e}")
                 raise e


async def setup(bot):
    await bot.add_cog(UnbanCog(bot))
