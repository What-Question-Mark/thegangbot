import discord, asyncio, random, time, json, os, string, aiohttp, re, openai, urllib.parse
from discord.ext import commands
from discord.utils import get

f = open('config.json')
config = json.load(f)
openai.api_key = config["OPENAI"]

messages = [
    {
        "role": "system",
        "content": "You are a user in a discord server."
    }
]

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

class AI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="chatgpt", description="Ask chatgpt something")
    async def chatgpt(self, ctx:discord.ApplicationContext, message):
        try:
            messages.append(
                {"role": "user", "content": message},
            )
            chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", 
                messages=messages
            )
            await ctx.respond(chat.choices[0].message.content)
        except Exception as e:
            embed=discord.Embed(color=colours["RED"])
            embed.add_field(name="Failed", value=f"```py\n{e}\n```", inline=True)
            await ctx.respond(embed=embed)

    @commands.slash_command(name="resetchatcontext", description="Reset the chat")
    async def resetchatcontext(self, ctx:discord.ApplicationContext):
        try:
            messages.clear()
            messages.append(
                {"role": "user", "content": "You are a user in a discord server."}
            )
            await ctx.respond("Reset chat!")
        except Exception as e:
            embed=discord.Embed(color=colours["RED"])
            embed.add_field(name="Failed", value=f"```py\n{e}\n```", inline=True)
            await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(AI(bot))