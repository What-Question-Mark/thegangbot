import discord, asyncio, random, time, json, os, string, aiohttp, re, openai, urllib.parse
from discord.ext import commands
from discord.utils import get

topics = [
    "What are some of your favorite hobbies or interests?",
    "Have you read any good books, watched any good movies or TV shows lately?",
    "What are your favorite video games, and why?",
    "What are your favorite types of music or artists/bands?",
    "What are some of your favorite travel destinations?",
    "What are some of your favorite restaurants or types of food?",
    "What are your thoughts on current events or news stories?",
    "What are some interesting facts about yourself that not many people know?",
    "What are your favorite memes or internet trends?",
    "What are some funny or embarrassing stories from your past?",
    "What are your favorite podcasts or YouTubers?",
    "What are some of your favorite memories with 'The Gang'?",
    "What are some of your goals or aspirations for the future?",
    "What are some interesting or unique experiences you've had?",
    "What are some of your favorite quotes or sayings?"
]

games = [
    "Fortnite",
    "Minecraft",
    "Grand Theft Auto V",
    "Call of Duty: Warzone",
    "Valorant",
    "League of Legends",
    "Apex Legends",
    "Overwatch",
    "PlayerUnknown's Battlegrounds (PUBG)",
    "Counter-Strike: Global Offensive (CS:GO)",
    "Dota 2",
    "Rocket League",
    "Rainbow Six Siege",
    "FIFA 21",
    "Among Us",
    "Genshin Impact",
    "Fall Guys",
    "World of Warcraft",
    "The Sims 4",
    "Hades"
]

coding_challenges = [
    "Write a program that prints the numbers from 1 to 100. But for multiples of three print 'Fizz' instead of the number and for the multiples of five print 'Buzz'. For numbers which are multiples of both three and five print 'FizzBuzz'",
    "Write a program that calculates the factorial of a given number",
    "Write a program that finds the largest and smallest numbers in a list",
    "Write a program that checks if a given string is a palindrome",
    "Write a program that counts the number of vowels in a given string",
    "Write a program that counts the number of words in a given string",
    "Write a program that finds the most common word in a given string",
    "Write a program that sorts a list of integers in ascending order",
    "Write a program that sorts a list of integers in descending order",
    "Write a program that checks if a given number is prime",
    "Write a program that finds all prime numbers in a given range",
    "Write a program that converts a decimal number to binary",
    "Write a program that converts a binary number to decimal",
    "Write a program that calculates the Fibonacci sequence",
    "Write a program that calculates the sum of all even numbers in a given range",
    "Write a program that calculates the sum of all odd numbers in a given range",
    "Write a program that finds the second largest number in a list",
    "Write a program that checks if a given string contains only digits",
    "Write a program that checks if a given string contains only alphabets",
    "Write a program that generates a random password of a given length",
    "Write a program that checks if a given year is a leap year",
    "Write a program that checks if a given string is an anagram",
    "Write a program that reverses a given string",
    "Write a program that checks if a given string is a pangram",
    "Write a program that calculates the area of a triangle",
    "Write a program that calculates the area of a circle",
    "Write a program that calculates the area of a rectangle",
    "Write a program that calculates the area of a square",
    "Write a program that calculates the perimeter of a triangle",
    "Write a program that calculates the perimeter of a circle",
    "Write a program that calculates the perimeter of a rectangle",
    "Write a program that calculates the perimeter of a square",
    "Write a program that checks if a given number is a power of two",
    "Write a program that checks if a given number is a perfect square",
    "Write a program that finds the largest palindrome made from the product of two n-digit numbers",
    "Write a program that finds the sum of all the multiples of 3 or 5 below a given number",
    "Write a program that prints the first n prime numbers",
    "Write a program that finds the largest prime factor of a given number",
    "Write a program that checks if a given string is a valid email address",
    "Write a program that checks if a given number is an Armstrong number",
    "Write a program that finds the GCD (Greatest Common Divisor) of two given numbers",
    "Write a program that finds the LCM (Least Common Multiple) of two given numbers",
    "Write a program that sorts a list of strings in alphabetical order",
    "Write a program that removes duplicates from a given list",
    "Write a program that finds the kth largest element in a list",
    "Write a program that checks if a given number is a palindrome"
]

languages = [
    'Java', 
    'Python', 
    'JavaScript', 
    'C++', 
    'C', 
    'Ruby', 
    'PHP', 
    'SQL', 
    'C#', 
    'Go', 
    'Perl', 
    'R', 
    'Lua', 
    'Dart', 
    'TypeScript', 
    'Rust'
]

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

class Bored(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(name="topic", description="dead chat?")
    async def topic(self, ctx:discord.ApplicationContext):
        try:
            await ctx.respond(random.choice(topics))
        except Exception as e:
            embed=discord.Embed(color=colours["RED"])
            embed.add_field(name="Failed", value=f"```py\n{e}\n```", inline=True)
            await ctx.respond(embed=embed)
    
    @commands.slash_command(name="randomgame", description="bored asf?")
    async def randomgame(self, ctx:discord.ApplicationContext):
        try:
            await ctx.respond(random.choice(games))
        except Exception as e:
            embed=discord.Embed(color=colours["RED"])
            embed.add_field(name="Failed", value=f"```py\n{e}\n```", inline=True)
            await ctx.respond(embed=embed)
    
    @commands.slash_command(name="codingchallange", description="get better at coding")
    async def codingchallange(self, ctx:discord.ApplicationContext):
        try:
            await ctx.respond(f"{random.choice(coding_challenges)} in {random.choice(languages)}")
        except Exception as e:
            embed=discord.Embed(color=colours["RED"])
            embed.add_field(name="Failed", value=f"```py\n{e}\n```", inline=True)
            await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Bored(bot))