import discord, asyncio, random, time, json, os, sys, string, aiohttp, re, openai, urllib.parse
from discord.ext import commands
from discord.utils import get
from discord.ui import View, Button, Select

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

class colors:
    END = '\033[0m'
    FAIL = '\033[91m'
    OKGREEN = '\033[92m'
    OKYELLOW = '\033[93'
    OKBLUE = '\033[94m'
    OKPINK = '\033[95m'

class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(name="purge", description="Someone annoying?")
    async def purge(self, ctx:discord.ApplicationContext, amount:int, user:discord.User=None):
        try:
            if amount > 25:
                embed=discord.Embed(color=colours["RED"])
                embed.add_field(name="Failed", value=f"```py\nToo big of an amount\n```", inline=True)
                await ctx.respond(embed=embed)
            if amount <= 0:
                embed=discord.Embed(color=colours["RED"])
                embed.add_field(name="Failed", value=f"```py\nToo little of an amount\n```", inline=True)
                await ctx.respond(embed=embed)
            else:
                if user == None:
                    await ctx.channel.purge(limit=amount)
                    await ctx.respond(f"Deleted {amount} messages")
                else:
                    await ctx.channel.purge(limit=amount, check=lambda msg: msg.author.id == user.id)
                    await ctx.respond(f"Deleted {amount} messages from {user}")
        except Exception as e:
            embed=discord.Embed(color=colours["RED"])
            embed.add_field(name="Failed", value=f"```py\n{e}\n```", inline=True)
            await ctx.respond(embed=embed)
    
    @commands.slash_command(name="suicide", description="SOMETHING BAD HAPPENED!!!")
    async def suidice(self, ctx:discord.ApplicationContext):
        try:            
            if ctx.author.id in config["OWNER"]:
                embed=discord.Embed(title="WARNING", description="Are you sure you want to do this?", color=colours["RED"])
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1018326384860467300/1095558188759253054/siren.gif")
                
                button_confirm = Button(emoji="<:tick:1095563360575164426>", style=discord.ButtonStyle.red, disabled=False)
                button_deny = Button(emoji="<:x_:1095563373619466380>", style=discord.ButtonStyle.green, disabled=False)

                async def button_confirm_callback(interaction):
                    if interaction.user.id != ctx.author.id:
                        embed=discord.Embed(title="Failed", color=colours["RED"])
                        embed.add_field(name="Response:", value=f"```py\n{interaction.author}, you are not allowed to do this\n```", inline=False)
                        await interaction.followup.send(embed=embed)
                    else:
                        await interaction.response.edit_message(content="", embed=discord.Embed(title="Exiting all processes...", color=colours["RED"]), view=None)
                        exit()

                async def button_deny_callback(interaction):
                    if interaction.user.id != ctx.author.id:
                        embed=discord.Embed(title="Failed", color=colours["RED"])
                        embed.add_field(name="Response:", value=f"```py\n{interaction.author}, you are not allowed to do this\n```", inline=False)
                        await interaction.followup.send(embed=embed)
                    else:
                        await interaction.response.edit_message(content="", embed=discord.Embed(title="Cancelled", color=colours["GREEN"]), view=None)
                
                button_confirm.callback = button_confirm_callback
                button_deny.callback = button_deny_callback

                view=View()
                view.add_item(button_confirm)
                view.add_item(button_deny)

                await ctx.respond(embed=embed, view=view)
            else:
                embed=discord.Embed(title="Failed", color=colours["RED"])
                embed.add_field(name="Response:", value=f"```py\nYou are not allowed to do this\n```", inline=False)
                await ctx.respond(embed=embed)
        except Exception as e:
            embed=discord.Embed(color=colours["RED"])
            embed.add_field(name="Failed", value=f"```py\n{e}\n```", inline=True)
            await ctx.respond(embed=embed)
    
    @commands.slash_command(name="restart", description="Restart the bot")
    async def restart(self, ctx:discord.ApplicationContext):
        try:            
            if ctx.author.id in config["OWNER"]:
                embed=discord.Embed(title="WARNING", description="Are you sure you want to do this?", color=colours["RED"])
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1018326384860467300/1095558188759253054/siren.gif")
                
                button_confirm = Button(emoji="<:tick:1095563360575164426>", style=discord.ButtonStyle.red, disabled=False)
                button_deny = Button(emoji="<:x_:1095563373619466380>", style=discord.ButtonStyle.green, disabled=False)

                async def button_confirm_callback(interaction):
                    if interaction.user.id != ctx.author.id:
                        embed=discord.Embed(title="Failed", color=colours["RED"])
                        embed.add_field(name="Response:", value=f"```py\n{interaction.author}, you are not allowed to do this\n```", inline=False)
                        await interaction.followup.send(embed=embed)
                    else:
                        await interaction.response.edit_message(content="", embed=discord.Embed(title="Restarting all processes...", color=colours["RED"]), view=None)
                        os.execl(sys.executable, sys.executable, * sys.argv)

                async def button_deny_callback(interaction):
                    if interaction.user.id != ctx.author.id:
                        embed=discord.Embed(title="Failed", color=colours["RED"])
                        embed.add_field(name="Response:", value=f"```py\n{interaction.author}, you are not allowed to do this\n```", inline=False)
                        await interaction.followup.send(embed=embed)
                    else:
                        await interaction.response.edit_message(content="", embed=discord.Embed(title="Cancelled", color=colours["GREEN"]), view=None)
                
                button_confirm.callback = button_confirm_callback
                button_deny.callback = button_deny_callback

                view=View()
                view.add_item(button_confirm)
                view.add_item(button_deny)

                await ctx.respond(embed=embed, view=view)
            else:
                embed=discord.Embed(title="Failed", color=colours["RED"])
                embed.add_field(name="Response:", value=f"```py\nYou are not allowed to do this\n```", inline=False)
                await ctx.respond(embed=embed)
        except Exception as e:
            embed=discord.Embed(color=colours["RED"])
            embed.add_field(name="Failed", value=f"```py\n{e}\n```", inline=True)
            await ctx.respond(embed=embed)

    @commands.slash_command(name="consolechat", description="Chat in the console")
    @commands.is_owner()
    async def consolechat(self, ctx:discord.ApplicationContext):
        try:            
            if ctx.author.id in config["OWNER"]:
                print("\n")

                await ctx.respond("Console Chat Activated", ephemeral=True)

                while True:
                    newMsg = input(f"{colors.OKPINK}$ {colors.END}")

                    if newMsg == ".exit":
                        break
                    if newMsg.startswith(".eval"):
                        evalText = newMsg.replace(".eval", "")
                        await eval(evalText)
                        continue
                    else:
                        await ctx.send(newMsg)
            else:
                embed=discord.Embed(title="Failed", color=colours["RED"])
                embed.add_field(name="Response:", value=f"```py\nYou are not allowed to do this\n```", inline=False)
                await ctx.respond(embed=embed)
        except Exception as e:
            embed=discord.Embed(color=colours["RED"])
            embed.add_field(name="Failed", value=f"```py\n{e}\n```", inline=True)
            await ctx.respond(embed=embed, ephemeral=True)

def setup(bot):
    bot.add_cog(Utils(bot))