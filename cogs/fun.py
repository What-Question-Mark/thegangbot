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

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="ararou", description="Ararou")
    async def ararou(self, ctx:discord.ApplicationContext, message=None):
        try:
            if message == None: 
                message = "meow"
            await ctx.respond(f"*~{message}*")
        except Exception as e:
            embed=discord.Embed(color=colours["RED"])
            embed.add_field(name="Failed", value=f"```py\n{e}\n```", inline=True)
            await ctx.respond(embed=embed)

    @commands.slash_command(name="echo", description="Display message on screen, writes each given STRING to standard output.")
    async def echo(self, ctx:discord.ApplicationContext, message):
        try:
            await ctx.respond(f"{message}")
        except Exception as e:
            embed=discord.Embed(color=colours["RED"])
            embed.add_field(name="Failed", value=f"```py\n{e}\n```", inline=True)
            await ctx.respond(embed=embed)

    @commands.slash_command(name="j", description="/j")
    async def j(self, ctx:discord.ApplicationContext, message=None):
        try:
            if message == None: 
                message = " "
            await ctx.respond(f"{message} /j")
        except Exception as e:
            embed=discord.Embed(color=colours["RED"])
            embed.add_field(name="Failed", value=f"```py\n{e}\n```", inline=True)
            await ctx.respond(embed=embed)

    @commands.slash_command(name="raisedeyebrow", description="🤨")
    async def raisedeyebrow(self, ctx:discord.ApplicationContext, message=None):
        try:
            if message == None: 
                message = " "
            await ctx.respond(f"{message} 🤨")
        except Exception as e:
            embed=discord.Embed(color=colours["RED"])
            embed.add_field(name="Failed", value=f"```py\n{e}\n```", inline=True)
            await ctx.respond(embed=embed)

    @commands.slash_command(name="nutrate", description="yeah i copied it from splinter.")
    async def nutrate(self, ctx:discord.ApplicationContext, user:discord.User=None):
        try:
            if user == None:
                user = ctx.author
            embed = discord.Embed(title=f"I rate {user.name}'s nuts a {random.randint(-1, 10)}/10", color=colours["TEAL"])
            await ctx.respond(embed=embed)
        except Exception as e:
            embed=discord.Embed(color=colours["RED"])
            embed.add_field(name="Failed", value=f"```py\n{e}\n```", inline=True)
            await ctx.respond(embed=embed)

    @commands.slash_command(name="susrate", description="red sus")
    async def susrate(self, ctx:discord.ApplicationContext, user:discord.User=None):
        try:
            if user == None:
                user = ctx.author
            embed = discord.Embed(title=f"{user.name} is {random.randint(0, 100)}% sus", color=colours["TEAL"])
            await ctx.respond(embed=embed)
        except Exception as e:
            embed=discord.Embed(color=colours["RED"])
            embed.add_field(name="Failed", value=f"```py\n{e}\n```", inline=True)
            await ctx.respond(embed=embed)

    @commands.slash_command(name="cat", description="A random photo of a cat")
    async def cat(self, ctx:discord.ApplicationContext):
        try:
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/animal/cat") as r:
                    res = await r.json()
            em = discord.Embed(color=colours["TEAL"])
            em.add_field(name="Fun Fact:", value=res["fact"])
            em.set_image(url=res["image"])
            await ctx.respond(embed=em)
        except Exception as e:
            embed=discord.Embed(color=colours["RED"])
            embed.add_field(name="Failed", value=f"```py\n{e}\n```", inline=True)
            await ctx.respond(embed=embed)

    @commands.slash_command(name="dog", description="A random photo of a dog")
    async def dog(self, ctx:discord.ApplicationContext):
        try:
            async with aiohttp.ClientSession() as cs:
                async with cs.get('https://some-random-api.ml/animal/dog') as r:
                    res = await r.json()
            em = discord.Embed(color=colours["TEAL"])
            em.add_field(name="Fun Fact:", value=res["fact"])
            em.set_image(url=res['image'])
            await ctx.respond(embed=em)
        except Exception as e:
            embed=discord.Embed(color=colours["RED"])
            embed.add_field(name="Failed", value=f"```py\n{e}\n```", inline=True)
            await ctx.respond(embed=embed)

    @commands.slash_command(name="bird", description="A random photo of a bird")
    async def bird(self, ctx:discord.ApplicationContext):
        try:
            async with aiohttp.ClientSession() as cs:
                async with cs.get('https://some-random-api.ml/animal/bird') as r:
                    res = await r.json()
            em = discord.Embed(color=colours["TEAL"])       
            em.add_field(name="Fun Fact:", value=res["fact"])
            em.set_image(url=res['image'])
            await ctx.respond(embed=em)
        except Exception as e:
            embed=discord.Embed(color=colours["RED"])
            embed.add_field(name="Failed", value=f"```py\n{e}\n```", inline=True)
            await ctx.respond(embed=embed)

    @commands.slash_command(name="tweet", description="Just like twitter.com")
    async def tweet(self, ctx:discord.ApplicationContext, user:discord.User, message):
        try:
            em = discord.Embed(color=colours["TEAL"])       
            em.set_image(url=f'https://some-random-api.ml/canvas/misc/tweet?comment={urllib.parse.quote(message)}&avatar={user.avatar}&username={user.name}&displayname={user}')
            await ctx.respond(embed=em)
        except Exception as e:
            embed=discord.Embed(color=colours["RED"])
            embed.add_field(name="Failed", value=f"```py\n{e}\n```", inline=True)
            await ctx.respond(embed=embed)

    @commands.slash_command(name="jail", description="You are under arrest!")
    async def jail(self, ctx:discord.ApplicationContext, user:discord.User):
        try:
            em = discord.Embed(color=colours["TEAL"])       
            em.set_image(url=f'https://some-random-api.ml/canvas/overlay/jail?avatar={user.avatar}')
            await ctx.respond(embed=em)
        except Exception as e:
            embed=discord.Embed(color=colours["RED"])
            embed.add_field(name="Failed", value=f"```py\n{e}\n```", inline=True)
            await ctx.respond(embed=embed)

    @commands.slash_command(name="megamind", description="No bitches?")
    async def megamind(self, ctx:discord.ApplicationContext, message):
        try:
            em = discord.Embed(color=colours["TEAL"])       
            em.set_image(url=f'https://some-random-api.ml/canvas/misc/nobitches?no={urllib.parse.quote(message)}')
            await ctx.respond(embed=em)
        except Exception as e:
            embed=discord.Embed(color=colours["RED"])
            embed.add_field(name="Failed", value=f"```py\n{e}\n```", inline=True)
            await ctx.respond(embed=embed)

    @commands.slash_command(name="joke", description="Funi")
    async def joke(self, ctx:discord.ApplicationContext):
        try:
            async with aiohttp.ClientSession() as cs:
                async with cs.get('https://some-random-api.ml/others/joke') as r:
                    res = await r.json()
            em = discord.Embed(title=res["joke"], color=colours["TEAL"]) 
            await ctx.respond(embed=em)
        except Exception as e:
            embed=discord.Embed(color=colours["RED"])
            embed.add_field(name="Failed", value=f"```py\n{e}\n```", inline=True)
            await ctx.respond(embed=embed)

    @commands.slash_command(name="lyrics", description="I love music")
    async def lyrics(self, ctx:discord.ApplicationContext, song:str):
        try:
            async with aiohttp.ClientSession() as cs:
                async with cs.get(f'https://some-random-api.ml/others/lyrics?title={urllib.parse.quote(song)}') as r:
                    res = await r.json()
            em = discord.Embed(title=f"{res['title']} by {res['author']} lyrics", description=res["lyrics"], color=colours["TEAL"]) 
            em.set_thumbnail(url=res["thumbnail"]["genius"])
            em.set_footer(text=res["disclaimer"])
            await ctx.respond(embed=em)      
        except Exception as e:
            embed=discord.Embed(color=colours["RED"])
            embed.add_field(name="Failed", value=f"```py\n{e}\n```", inline=True)
            await ctx.respond(embed=embed)

    @commands.slash_command(name="pokedex", description="PIKACHU")
    async def pokedex(self, ctx:discord.ApplicationContext, pokemon:str):
        try:
            async with aiohttp.ClientSession() as cs:
                async with cs.get(f'https://some-random-api.ml/pokemon/pokedex?pokemon={pokemon}'.replace(' ', '%20')) as r:
                    res = await r.json()
            em = discord.Embed(title=res["name"], description=res["description"], color=colours["TEAL"])
            em.add_field(name="Height", value=res["height"], inline=True)
            em.add_field(name="Weight", value=res["weight"], inline=True)
            em.add_field(name="Base XP", value=res["base_experience"], inline=True)
            em.add_field(name="Stats", value="", inline=False)
            em.add_field(name="HP", value=res["stats"]["hp"], inline=True)
            em.add_field(name="Attack", value=res["stats"]["attack"], inline=True)
            em.add_field(name="Defense", value=res["stats"]["defense"], inline=True)
            em.set_thumbnail(url=res["sprites"]["animated"])
            em.set_footer(text=f"ID: {res['id']} | Generation: {res['generation']}")
            await ctx.respond(embed=em)        
        except Exception as e:
            embed=discord.Embed(color=colours["RED"])
            embed.add_field(name="Failed", value=f"**{pokemon}** isn't a pokemon | Make sure you spelled it correctly.", inline=True)
            await ctx.respond(embed=embed)

    @commands.slash_command(name="tokengrabber", description="joke btw")
    async def tokengrabber(self, ctx:discord.ApplicationContext, bot:discord.User):
        try:
            if bot.bot:
                async with aiohttp.ClientSession() as cs:
                    async with cs.get(f'https://some-random-api.ml/others/bottoken?id={bot.id}') as r:
                        res = await r.json()
                em = discord.Embed(title=f"{bot}'s token", description=res["token"], color=colours["TEAL"]) 
                await ctx.respond(embed=em)
            else:
                embed=discord.Embed(color=colours["RED"])
                embed.add_field(name="Failed", value=f"User is not a bot", inline=True)
                await ctx.respond(embed=embed)
        except Exception as e:
            embed=discord.Embed(color=colours["RED"])
            embed.add_field(name="Failed", value=f"```py\n{e}\n```", inline=True)
            await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Fun(bot))