import discord, asyncio, random, time, json, os, string, aiohttp, re, openai, urllib.parse
from discord.ext import commands
from discord.utils import get

f = open('config.json')
config = json.load(f)

colours = {
    "RED": 0xf10f48,
    "ORANGE": 0xf1800e,
    "YELLOW": 0xF1C40F,
    "GREEN": 0x0ef16d,
    "TEAL": 0x0ef1de,
    "BLUE": 0x0ea5f1,
    "PURPLE": 0x920ef1,
    "PINK": 0xf10ef1
}

class Party(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="createparty", description="Create a game party")
    async def createparty(
        self, 
        ctx: discord.ApplicationContext, 
        game: discord.Option(
            str, 
            choices=[
                "Minecraft",
                "Fortnite",
                "GTA",
                "Roblox",
                "Rocket League",
                "Among Us",
                "Valorant",
                "None",
                "Other"
            ]
        ),
        userone: discord.User,
        usertwo: discord.User=None,
        userthree: discord.User=None
    ):
        try:
            channel = await ctx.guild.create_text_channel(name=f"party-{ctx.author.name}", category=self.bot.get_channel(1089074461921259581))
            await channel.send(content=f"{ctx.author.mention}, {userone.mention}{', '+usertwo.mention if usertwo is not None else ''}{', '+userthree.mention if userthree is not None else ''}", embed=discord.Embed(title=f"Welcome to {channel.mention}",color=colours["GREEN"]))

            embed=discord.Embed(color=colours["GREEN"])
            embed.add_field(name="Success", value=f"Created a party in {channel.mention}", inline=False)
            embed.add_field(name="Users", value=f"{ctx.author.mention}, {userone.mention}{', '+usertwo.mention if usertwo is not None else ''}{', '+userthree.mention if userthree is not None else ''}", inline=False)
            embed.set_footer(text="Can't see the channel? Go to 'Browse Channels' and follow 'Temporary Channels'")

            await ctx.respond(embed=embed)
        except Exception as e:
            embed=discord.Embed(color=colours["RED"])
            embed.add_field(name="Failed", value=f"```py\n{e}\n```", inline=True)
            await ctx.respond(embed=embed)

    @commands.slash_command(name="deleteparty", description="Delete a game party")
    async def deleteparty(self, ctx:discord.ApplicationContext):
        try:
            if ctx.channel.name.startswith("party-"):
                await ctx.channel.delete()
            else:
                embed=discord.Embed(color=colours["RED"])
                embed.add_field(name="Failed", value=f"```py\nChannel is not a party\n```", inline=False)

                await ctx.respond(embed=embed)
        except Exception as e:
            embed=discord.Embed(color=colours["RED"])
            embed.add_field(name="Failed", value=f"```py\n{e}\n```", inline=True)
            await ctx.respond(embed=embed)
            
def setup(bot):
    bot.add_cog(Party(bot))