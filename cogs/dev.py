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

start_time = time.time()

class Dev(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="eval", description="Evaluate some code")
    async def e(self, ctx:discord.ApplicationContext, *, code):
        try:
            if ctx.author.id in config["EVAL"]:
                try:
                    res = await eval(code)
                    embed=discord.Embed(title="Success", color=colours["GREEN"])
                    embed.add_field(name="Code:", value=f"```py\n{code}\n```", inline=False)
                    embed.add_field(name="Response:", value=f"```html\n{res}\n```", inline=False)
                    await ctx.respond(embed=embed)          
                except Exception as e:
                    embed=discord.Embed(title="Failed", color=colours["RED"])
                    embed.add_field(name="Code:", value=f"```py\n{code}\n```", inline=False)
                    embed.add_field(name="Response:", value=f"```py\n{e}\n```", inline=False)
                    await ctx.respond(embed=embed)
            else:
                embed=discord.Embed(title="Failed", color=colours["RED"])
                embed.add_field(name="Code:", value=f"```py\n{code}\n```", inline=False)
                embed.add_field(name="Response:", value=f"```py\nYou don't have permission to do this\n```", inline=False)
                await ctx.respond(embed=embed)
        except Exception as e:
            embed=discord.Embed(color=colours["RED"])
            embed.add_field(name="Failed", value=f"```py\n{e}\n```", inline=True)
            await ctx.respond(embed=embed)
            
    @commands.slash_command(name="ping", description="Get the ping of the bot")
    async def ping(self, ctx:discord.ApplicationContext):
        try:
            embed = discord.Embed(description=f"Pong 🏓 **|** `{round(self.bot.latency * 1000)}ms`", color=colours["BLUE"])
            await ctx.respond(embed=embed)
        except Exception as e:
            embed=discord.Embed(color=colours["RED"])
            embed.add_field(name="Failed", value=f"```py\n{e}\n```", inline=True)
            await ctx.respond(embed=embed)
            
    @commands.slash_command(name="uptime", description="Get the uptime of the bot")
    async def uptime(self, ctx:discord.ApplicationContext):
        try:
            embed = discord.Embed(description=f"The bot started <t:{round(start_time)}:R> 🕒", color=colours["BLUE"])
            await ctx.respond(embed=embed)
        except Exception as e:
            embed=discord.Embed(color=colours["RED"])
            embed.add_field(name="Failed", value=f"```py\n{e}\n```", inline=True)
            await ctx.respond(embed=embed)

    @commands.slash_command(name="help", description="Get a list of commands")
    async def help(self, ctx:discord.ApplicationContext):
        try:
            embed = discord.Embed(title="List of Commands", color=colours["BLUE"])
            embed.add_field(name="AFK", value="> `afk`", inline=False)
            embed.add_field(name="AI", value="> `chatgpt`, `resetchatcontext`", inline=False)
            embed.add_field(name="Bored", value="> `topic`, `randomgame`, `codingchallange`", inline=False)
            embed.add_field(name="Dev", value="> `eval`, `ping`, `help`", inline=False)
            embed.add_field(name="Fun", value="> `ararou`, `nutrate`, `susrate`, `cat`, `dog`, `bird`, `tweet`, `jail`, `megamind`, `joke`, `lyrics`, `pokedex`, `tokengrabber`", inline=False)
            embed.add_field(name="IRL", value="> `weather`, `news`, `dictionary`", inline=False)
            embed.add_field(name="Party", value="> `createparty`, `deleteparty`", inline=False)
            embed.set_footer(text="These are all slash commands (e.g. /help)")
            await ctx.respond(embed=embed)
        except Exception as e:
            embed=discord.Embed(color=colours["RED"])
            embed.add_field(name="Failed", value=f"```py\n{e}\n```", inline=True)
            await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Dev(bot))