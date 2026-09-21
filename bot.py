import os
import random
import discord
from discord.ext import commands

# =========================
# BOT SETUP
# =========================

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix=";",
    intents=intents
)


# =========================
# BOT READY
# =========================

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


# =========================
# BASIC COMMANDS
# =========================

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")


@bot.command()
async def hello(ctx):
    await ctx.send(f"yo {ctx.author.mention} 👋")


# =========================
# SAY COMMAND
# =========================

@bot.command()
@commands.has_permissions(administrator=True)
async def say(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(message)


# =========================
# AVATAR COMMAND
# =========================

@bot.command()
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author

    embed = discord.Embed(
        title=f"{member.display_name}'s avatar",
        color=discord.Color.blurple()
    )

    embed.set_image(url=member.display_avatar.url)

    await ctx.send(embed=embed)


# =========================
# SERVER ICON COMMAND
# =========================

@bot.command()
async def servericon(ctx):
    icon = ctx.guild.icon

    if icon:
        embed = discord.Embed(
            title=f"{ctx.guild.name}'s server icon",
            color=discord.Color.blurple()
        )

        embed.set_image(url=icon.url)

        await ctx.send(embed=embed)
    else:
        await ctx.send("this server doesn't have an icon 😭")


# =========================
# TUNG TUNG RESPONSES
# =========================

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
    "tung tung agrees 😭🙏",

    # MORE RANDOM RESPONSES
    "bro just spawned a whole side quest 😭",
    "i'm gonna need the entire backstory 💀",
    "this is getting out of hand 😭",
    "bro said that with confidence too 💀",
    "you really thought i wouldn't notice 😭",
    "that's one way to put it 💀",
    "i have several questions 😭🙏",
    "bro please explain yourself",
    "nah this needs further investigation 🕵️",
    "i'm not even gonna ask 😭",
    "that's between you and god bro 🙏",
    "you know what... fair 💀",
    "i'll pretend i didn't hear that 😭",
    "bro is NOT beating the allegations 💀",
    "the lore continues...",
    "another chapter has been added 😭",
    "this server has seen enough 💀",
    "bro unlocked a new dialogue option",
    "tung tung is taking notes 📝🗿",
    "tung tung is disappointed 😭",
    "tung tung has entered the chat 🗿",
    "tung tung is calculating...",
    "processing yap... ███████░░░ 73%",
    "yap detected 🚨",
    "maximum yap levels reached 😭",
    "bro has infinite dialogue",
    "this is premium yapping 💀",
    "keep cooking chef 🔥",
    "the kitchen is getting dangerous 😭",
    "bro is cooking without a recipe",
    "someone take bro's microphone 💀",
    "i fear you may be onto something",
    "wait... let him cook 👀",
    "bro might actually have a point 😭",
    "i'm invested unfortunately",
    "why am i actually interested in this 💀",
    "you got my attention now",
    "okay this is kinda fire 🔥",
    "nah that's actually valid",
    "i respect the vision 🫡",
    "questionable... but respectable 😭",
    "that's certainly a decision 💀",
    "bold strategy ngl",
    "you woke up and chose chaos 😭",
    "chaos detected 🚨",
    "bro chose violence today",
    "this is diabolical 💀",
    "i wasn't emotionally prepared for that 😭",
    "bro dropped that like it was normal",
    "HELLO?? 😭",
    "ain't no way 💀",
    "nah bro 😭🙏",
    "bro what are we doing",
    "i need a moment 💀",
    "give me a second to process this 😭",
    "my brain just blue screened",
    "tung tung.exe has stopped responding 💀",
    "system overload 😭",
    "critical lore detected 🚨",
    "lore accurate behavior",
    "character development?? 👀",
    "this is not in the script 😭",
    "bro skipped the tutorial",
    "side quest accepted 🫡",
    "main quest updated 📜",
    "new lore just dropped",
    "season finale type conversation 💀",
    "this deserves its own episode 😭",
    "bro is writing a whole arc",
    "i'm seated 🍿",
    "go ahead i'm listening",
    "continue the story 👀",
    "don't leave me on a cliffhanger 😭",
    "AND THEN??",
    "okay wait i'm actually curious",
    "tell me more before i judge 💀",
    "i'm listening... respectfully",
    "you have the floor 🎤",
    "the floor is yours",
    "speak your truth 😭🙏",
    "i support the yap",
    "yap responsibly 🙏",
    "certified yapper detected",
    "professional yapper behavior",
    "bro got the yap DLC 💀",
    "yapping premium unlocked",
    "tung tung gives this story a 10/10 🗿",
    "tung tung is invested now 😭",
    "tung tung says continue",
    "tung tung demands context",
    "tung tung does not understand 💀",
    "tung tung has questions",
    "tung tung approves this message 🗿",
    "tung tung is concerned for your wellbeing 😭",
    "bro has officially confused tung tung",
    "i'm gonna pretend that made sense 💀"
]


# =========================
# TUNG TUNG CONVERSATION
# =========================

@bot.event
async def on_message(message):

    # Ignore the bot itself
    if message.author == bot.user:
        return

    content = message.content.lower()

    # Start Tung Tung conversation
    if bot.user in message.mentions and "tung tung" in content:
        await message.channel.send(
            f"tung tung {message.author.mention} 😭 what's up?"
        )

    # Continue conversation when replying to the bot
    elif message.reference and message.reference.resolved:

        replied_message = message.reference.resolved

        if replied_message.author == bot.user:
            await message.channel.send(
                random.choice(responses)
            )

    # Keep normal commands working
    await bot.process_commands(message)


# =========================
# FUN COMMANDS
# =========================

@bot.command()
async def coinflip(ctx):
    result = random.choice([
        "heads 🪙",
        "tails 🪙"
    ])

    await ctx.send(f"it's **{result}**")


@bot.command()
async def dice(ctx):
    number = random.randint(1, 6)

    await ctx.send(
        f"🎲 you rolled **{number}**"
    )


@bot.command()
async def rate(ctx, *, thing):
    rating = random.randint(1, 10)

    await ctx.send(
        f"i rate **{thing}** a **{rating}/10** 😭"
    )


@bot.command()
async def ship(ctx, member1: discord.Member, member2: discord.Member):
    percentage = random.randint(0, 100)

    if percentage >= 80:
        response = "THEY'RE ACTUALLY COOKING 🔥❤️"

    elif percentage >= 50:
        response = "hmm there's potential 👀"

    elif percentage >= 20:
        response = "it's looking rough 😭"

    else:
        response = "bro just stay friends 💀"

    await ctx.send(
        f"💘 **{member1.display_name} + "
        f"{member2.display_name}** = "
        f"**{percentage}%**\n{response}"
    )


@bot.command()
async def eightball(ctx, *, question):
    answers = [
        "yes.",
        "no.",
        "probably 😭",
        "absolutely not 💀",
        "maybe 👀",
        "100%",
        "ask me later",
        "i wouldn't count on it 😭",
        "it's looking good",
        "bro idk 😭",
        "the answer is hidden...",
        "tung tung says yes 🗿",
        "tung tung says no 💀"
    ]

    await ctx.send(
        f"🎱 **{random.choice(answers)}**"
    )


@bot.command()
async def choose(ctx, *, options):
    choices = [
        x.strip()
        for x in options.split(",")
        if x.strip()
    ]

    if len(choices) < 2:
        await ctx.send(
            "give me at least 2 options 😭"
        )
        return

    choice = random.choice(choices)

    await ctx.send(
        f"i choose **{choice}** 👀"
    )


@bot.command()
async def roast(ctx, member: discord.Member = None):
    member = member or ctx.author

    roasts = [
        "bro's WiFi signal has more personality 😭",
        "you really woke up and chose to be like this 💀",
        "bro is built like a loading screen",
        "even Tung Tung doesn't know what to say 😭",
        "respectfully... log off 🙏",
        "your aura needs an update",
        "bro has negative aura points 💀",
        "i've seen NPCs with more dialogue 😭",
        "you are the reason the mute button exists",
        "bro's main character arc got cancelled"
    ]

    await ctx.send(
        f"{member.mention} {random.choice(roasts)}"
    )


@bot.command()
async def compliment(ctx, member: discord.Member = None):
    member = member or ctx.author

    compliments = [
        "you're actually cool ngl 🫶",
        "your aura is immaculate 🔥",
        "you seem like a genuinely good person",
        "certified W human 🫡",
        "you're carrying the server fr",
        "10/10 vibes",
        "you've got elite energy 😭🔥",
        "Tung Tung approves of you 🗿",
        "you're more awesome than you realize",
        "absolute W"
    ]

    await ctx.send(
        f"{member.mention} {random.choice(compliments)}"
    )


@bot.command()
async def wyr(ctx):
    questions = [
        "would you rather be able to fly or become invisible? 👀",
        "would you rather have unlimited money or unlimited free time?",
        "would you rather live in the ocean or in space? 🌊🚀",
        "would you rather never sleep again or never eat again?",
        "would you rather know your future or change your past?",
        "would you rather be famous or completely anonymous?",
        "would you rather have super strength or super speed?",
        "would you rather lose your phone or your wallet? 😭",
        "would you rather always be 10 minutes late or 20 minutes early?",
        "would you rather fight 100 duck-sized horses or 1 horse-sized duck? 💀"
    ]

    await ctx.send(
        random.choice(questions)
    )


# =========================
# START BOT
# =========================

bot.run(os.environ["DISCORD_TOKEN"])