import discord
from discord.ext import commands
from discord import app_commands
import json

class WelcomeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open('settings.json', 'r') as config_file:
            settings = json.load(config_file)
        
        
        welcome_channel_id = settings['channels']['welcome']

        channel = member.guild.get_channel(welcome_channel_id)
        if channel:
            
            welcome_embed = discord.Embed(title="",
                                          description=f"**🌷𝙒𝙚𝙡𝙘𝙤𝙢𝙚 {member.mention} 𝙩𝙤 Ritz's Server🌷**",
                                          color=discord.Color.purple())
            welcome_embed.add_field(name="", value="/) /) ~\n( •-• ) ~ ♡ 𝕐𝕠𝕦 𝕒𝕣𝕖 𝕒𝕞𝕒𝕫𝕚𝕟𝕘 ♡\n( •-• ) ~ ♡ ℝ𝕖𝕢𝕦𝕖𝕤𝕥 𝕣𝕠𝕝𝕖 <#1215361362495143991> ♡\n( •-• ) ~ ♡ ℂ𝕙𝕖𝕔𝕜 𝕊𝕖𝕝𝕗 ℝ𝕠𝕝𝕖𝕤 <#1215361362495143991> ♡\n( •-• ) ~ ♡ ℂ𝕙𝕖𝕔𝕜 ℝ𝕦𝕝𝕖𝕤 <#1215572335617253406> ♡\n/づづ ~ ꒰ 🍒 ꒱")
            welcome_embed.set_image(url="https://images-ext-2.discordapp.net/external/93-TNCFVkvbnZ73Hpj4XFa8aIrB2HkWklEo6qZtJAYQ/https/i.pinimg.com/originals/ee/21/b6/ee21b6f99f0effacee7f97699144b5f3.gif")
            await channel.send(embed=welcome_embed)

async def setup(bot):
    await bot.add_cog(WelcomeCog(bot))