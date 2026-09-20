import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=";", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

@bot.command()
async def hello(ctx):
    await ctx.send(f"yo {ctx.author.mention} 👋")

bot.run(os.environ["DISCORD_TOKEN"])
responses = [
    "lmao 😭 what you been doing today?",
    "real 😭 tell me more",
    "damn 💀 and then what happened?",
    "😭 nah fr",
    "interesting... continue 👀",
    "bro is actually yapping 😭🙏",
    "fair enough 😭",
    "so what's the plan then?",
    "wait what 😭",
    "no way bro 💀",
    "that's actually crazy 😭",
    "i'm listening 👀",
    "go on i'm invested now 😭",
    "bro really said that 💀",
    "hmm 🤔 elaborate",
    "and how does that make you feel 😭",
    "that's wild ngl",
    "😭😭 you're actually funny",
    "okay okay i hear you",
    "valid honestly 🙏",
    "nah you're onto something",
    "bro has lore 😭",
    "tell me everything 👀",
    "what happened after that?",
    "and then?? 😭",
    "no shot 💀",
    "bro what 😭🙏",
    "i wasn't expecting that",
    "interesting choice ngl 😭",
    "you can't just say that and leave 💀",
    "okay i'm invested now",
    "keep talking i'm listening 😭",
    "that's crazy work",
    "bro is cooking 💀",
    "let him cook 😭🙏",
    "i understand you 🫡",
    "honestly? real",
    "that's actually kinda crazy",
    "wait i need context 😭",
    "give me the lore",
    "there's no way 😭",
    "bro dropped the lore casually",
    "okay but why 😭",
    "what made you do that?",
    "and what did they say? 👀",
    "nah i'd be confused too 😭",
    "i see where you're coming from",
    "that's fair honestly",
    "you might have a point 👀",
    "😭 bro is onto something",
    "this conversation is getting interesting",
    "okay now i'm curious",
    "go deeper 😭",
    "say more",
    "i'm all ears 👂",
    "bro really came here to yap 😭",
    "and i'm here for it",
    "keep yapping 🙏",
    "never stop yapping 😭",
    "certified yap session",
    "tung tung approves 🗿",
    "tung tung has heard enough 😭",
    "tung tung is processing this information...",
    "tung tung is concerned 💀",
    "tung tung needs more context",
    "tung tung understands 🫡",
    "tung tung agrees 😭🙏"
]