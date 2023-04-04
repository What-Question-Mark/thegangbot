import discord, asyncio, random, time, json, os, string, aiohttp, re, openai, urllib.parse
from discord.ext import commands
from discord.utils import get
from discord.ui import View, Button, Select

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

class ButtonBack(Button):
    def __init__(self):
        super().__init__(emoji="⬅️", style=discord.ButtonStyle.blurple, disabled=False)
    
    async def callback(self, interaction):
        await interaction.followup.send_message(content="hi")

class ButtonNext(Button):
    def __init__(self):
        super().__init__(emoji="➡️", style=discord.ButtonStyle.blurple, disabled=False)

class ButtonGoto(Button):
    def __init__(self, url):
        super().__init__(label="Open Page", url=url)
    
    async def callback(self, interaction):
        await interaction.followup.send_message(content="bye")

class Irl(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(name="weather", description="Get weather")
    async def weather(self, ctx:discord.ApplicationContext, location):
        try:
            async with aiohttp.ClientSession() as cs:
                async with cs.get(f'https://api.weatherapi.com/v1/current.json?key={config["WEATHER"]}&q={location}&aqi=no') as r:
                    res = await r.json()

            embed=discord.Embed(title=f"{res['location']['name']} - {res['location']['country']}", description=res["location"]["region"], color=colours["GREEN"])
            embed.add_field(name="Temperature", value=f'{res["current"]["temp_c"]}℃ - {res["current"]["temp_f"]}℉', inline=True)
            embed.add_field(name="Condition", value=res["current"]["condition"]["text"], inline=True)
            embed.add_field(name="UV", value=f"{res['current']['humidity']}%", inline=True)
            embed.add_field(name="Humidity", value=res["current"]["uv"], inline=True)
            embed.set_thumbnail(url="https:"+res["current"]["condition"]["icon"])
            embed.set_footer(text="Powered by WeatherAPI.com")
            
            await ctx.respond(embed=embed)
        except Exception as e:
            embed=discord.Embed(color=colours["RED"])
            embed.add_field(name="Failed", value=f"```py\n{e}\n```", inline=True)
            await ctx.respond(embed=embed)
    
    @commands.slash_command(name="news", description="real stuff")
    async def news(self, ctx:discord.ApplicationContext):
        i = 0
        try:
            async with aiohttp.ClientSession() as cs:
                async with cs.get(f'https://api.nytimes.com/svc/topstories/v2/home.json?api-key={config["NEWS"]}') as r:
                    res = await r.json()

            embed=discord.Embed(title=f"{res['results'][i]['title']}", description=res['results'][i]['abstract'], color=colours["GREEN"])
            embed.set_thumbnail(url=res['results'][i]['multimedia'][2]["url"])
            embed.set_image(url=res['results'][i]['multimedia'][0]['url'])
            embed.set_footer(text=res["copyright"])

            '''
            button_back = ButtonBack()
            button_goto = ButtonGoto(res["results"][i]["url"])
            button_next = ButtonNext()
            '''

            view=View()
            '''
            view.add_item(button_back)
            view.add_item(button_goto)
            view.add_item(button_next)
            '''

            await ctx.respond(embed=embed, view=view)
        except Exception as e:
            embed=discord.Embed(color=colours["RED"])
            embed.add_field(name="Failed", value=f"```py\n{e}\n```", inline=True)
            await ctx.respond(embed=embed)
    
    @commands.slash_command(name="dictionary", description="Define a word")
    async def dictionary(self, ctx:discord.ApplicationContext, word):
        try:
            async with aiohttp.ClientSession() as cs:
                async with cs.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}') as r:
                    res = await r.json()

            embed=discord.Embed(title=res[0]['word'].capitalize(), description=res[0]['phonetics'][1]['text'], color=colours["GREEN"])

            for meaning in res[0]['meanings']: 
                for definition in meaning['definitions']:
                    embed.add_field(name=meaning['partOfSpeech'].capitalize(), value=definition['definition'], inline=False)

            embed.set_footer(text="Powered by DictionaryAPI.dev")

            await ctx.respond(embed=embed)
        except Exception as e:
            embed=discord.Embed(color=colours["RED"])
            embed.add_field(name="Failed", value=f"```py\n{e}\n```", inline=True)
            await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Irl(bot))