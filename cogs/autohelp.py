import discord, asyncio, random, time, json, os, string, aiohttp, re, openai, urllib.parse
from discord.ext import commands
from discord.utils import get
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

f = open('config.json')
config = json.load(f)

questions = [
    "What is your return policy?",
    "How long does it take to ship?",
    "What payment methods do you accept?",
    "How do I reset my password?",
    "Can I cancel my order?",
]

answers = [
    "Our return policy is 30 days.",
    "Shipping usually takes 3-5 business days.",
    "We accept credit cards, PayPal, and Apple Pay.",
    "To reset your password, go to the login page and click 'Forgot Password'.",
    "Yes, you can cancel your order within 24 hours of placing it.",
]

vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)

def get_matching_question(input_question):
    input_vector = vectorizer.transform([input_question])
    similarities = cosine_similarity(input_vector, question_vectors)
    closest_question_index = similarities.argmax()
    return questions[closest_question_index]

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

class AutoHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):   
        if self.bot.user.mentioned_in(message):
            input_question = message.content.replace("", "")
            matching_question = get_matching_question(input_question)
            matching_answer = answers[questions.index(matching_question)]
            await message.reply(matching_answer)
        else:
            pass

def setup(bot):
    bot.add_cog(AutoHelp(bot))