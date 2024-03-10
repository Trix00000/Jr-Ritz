import discord
from discord.ext import commands
from discord import app_commands,  ui

class BanCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ban", description="Ban a member from the server")
    @app_commands.describe(user="The user you want to ban", reason="Why you are banning this user?")
    @app_commands.checks.has_permissions(administrator=True)
    async def ban(self, interaction: discord.Interaction, user: discord.Member, reason:str="No reason given"):
        YesButton = ui.Button(label='Yes', custom_id='yes', style=discord.ButtonStyle.green)
        view = ui.View(timeout=None)
        view.add_item(YesButton)
        author = interaction.user.id
        embed = discord.Embed(title="Are you sure about that? This action is irreversible!",
                              description=f"**Action:** **`ban`**\n**User:** {user.mention}\n**Reason:** `{reason}`",
                              color=discord.Color.red())
        await interaction.response.send_message(embed=embed, view=view)

        async def Yes_callback(interaction: discord.Interaction):
            if  interaction.user.id == author:
                try:
                    await user.ban(reason=reason)
                    embed = discord.Embed(description=f"Successfully Banned `{user}` for `{reason}`.", color=0x57ff6a)
                    await interaction.response.send_message(embed=embed)
                except Exception as e:
                    error_embed = discord.Embed(description=f"an error occured: `{e}`",
                                                color=discord.Color.red())
                    await interaction.response.send_message(embed=error_embed)

            else:
                await interaction.followup.send("You can't do this action.", ephemeral=True)

        YesButton.callback = Yes_callback





async def setup(bot):
    await bot.add_cog(BanCog(bot))
