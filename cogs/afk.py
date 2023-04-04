import discord, asyncio, random, time, json, os, string, aiohttp, re, openai, urllib.parse
from discord.ext import commands
from discord.utils import get

f = open('config.json')
config = json.load(f)

afk_dict = {}

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

class Afk(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(name="afk", description="Going out side?")
    async def afk(self, ctx:discord.ApplicationContext, reason=None):
        try:
            afk_dict[ctx.user.id] = reason
            await ctx.respond("You are now afk. Beware of the real world!")
        except Exception as e:
            embed=discord.Embed(color=colours["RED"])
            embed.add_field(name="Failed", value=f"```py\n{e}\n```", inline=True)
            await ctx.respond(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):    
        if message.author.id == 1089061324295770173:
            pass
        else:
            if message.author.id in afk_dict:
                await message.reply(f"Welcome back!", mention_author=False)
                afk_dict.pop(message.author.id)
            for user in message.mentions:
                if user.id not in afk_dict:
                    continue
                reason = afk_dict[user.id] or ""
                await message.reply(f"That user is afk.", mention_author=False)

def setup(bot):
    bot.add_cog(Afk(bot))