import discord, asyncio, random, time, json, os, string, aiohttp, re, openai, urllib.parse
from discord import File
from discord.ext import commands
from discord.utils import get
import chess, chess.svg
from cairosvg import svg2png
from PIL import Image

f = open('config.json')
config = json.load(f)

board_colours = {
    "square light": "#FFFFFF",
    "square dark": "#5865F2",
    "square light lastmove": "#454FBF",
    "square dark lastmove": "#454FBF"
}

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

class Chess(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    '''
    @commands.slash_command(name="chess", description="play chess")
    async def chess(self, ctx:discord.ApplicationContext):
        try:
            board = chess.Board()
            chess_author = ctx.author.id
            svg2png(bytestring=chess.svg.board(board, colors=board_colours), write_to='chess.png')
            await ctx.respond("Made chess game", ephemeral=True)
            chess_message = await ctx.send(file=File('chess.png'))

            def check(m):
                return m.content.startswith("chess:") and m.author.id == ctx.author.id and m.channel.id == ctx.channel.id

            while True:
                msg = await self.bot.wait_for("message", check=check)

                content = msg.content.replace("chess:", "")

                if content.startswith("moves" or "legalmoves" or "legalmove"):
                    await ctx.send(board.legal_moves)
                    await msg.delete()
                    break

                elif content.startswith("move"):
                    if content.startswith("move="):
                        if chess.Move.from_uci(content.replace("move=", "")) in board.legal_moves:
                            move = chess.Move.from_uci(content.replace("move=", ""))
                            board.push(move)

                            svg2png(bytestring=chess.svg.board(board, colors=board_colours), write_to='chess.png')

                            for file in chess_message.attachments:
                                file.remove()
                            await chess_message.edit(file=File('chess.png'))
                            await msg.delete()
                        else:
                            await ctx.send("That is an illegal move!")
                            await msg.delete()
                    else:
                        await msg.delete()
                        await ctx.send("You need to provide a move (e.g. chess:move=d4)")

                elif content.startswith("exit" or "end" or "stop"):
                    await ctx.send("Stoped the game of chess!")
                    await msg.delete()
                    break

        except Exception as e:
            embed=discord.Embed(color=colours["RED"])
            embed.add_field(name="Failed", value=f"```py\n{e}\n```", inline=True)
            await ctx.respond(embed=embed)
    '''

def setup(bot):
    bot.add_cog(Chess(bot))