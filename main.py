import discord
import asyncio
import random
from discord.ext import commands
from discord.ext.commands import CommandNotFound

token = 'Your token here!'

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
# bot = discord.Client()
bot = commands.Bot(command_prefix='!', intents=intents)

# Variables needed for the formatted strings
text = 'This is **Biology Class**: '
text1 = 'This is **English for Academic and Professional Purposes Class**: '
text2 = 'This is **Physics Class**: '
text3 = 'This is **Entrepreneurship Class**: '
text4 = 'This is **Homeroom**: '
text5 = 'This is **Guidance**: '
text6 = 'Here is your class schedule for this term. Enjoy Learning! '
text7 = "Stay updated with Elizabeth Seton School's Facebook Page: "
text8 = "Check out the official website of Elizabeth Seton School: "
text9 = "**MEGA**: "
text10 = "**GOOGLE DRIVE**: "
text11 = "**DROPBOX**: "
text12 = "**MICROSOFT ONEDRIVE**: "
text13 = "**PASTEBIN**: "
text14 = "**ESS BOT OFFICIAL GITHUB REPOSITORY:**"


# Checks if the Bot is ready
@bot.event
async def on_ready():
    print('--------------------------')
    print('The Bot is ready!')
    print(bot.user.name)
    print(bot.user.id)
    print('--------------------------')


# This godsend error handler to avoid "COMMAND NOT FOUND" false positive.
@bot.event
async def on_command_error(error):  # if it does not work, try (ctx, error)
    if isinstance(error, CommandNotFound):
        return
    raise error


# Terminal CMD Logging
# Shows the members and Guilds (Servers) added or removed
@bot.event
async def on_member_join(member):
    print(f'{member} has joined the server.')


@bot.event
async def on_member_remove(member):
    print(f'{member} has left the server.')


@bot.event
async def on_guild_join(guild):
    print(f'We have been added by {guild}!')


@bot.event
async def on_guild_remove(guild):
    print(f'We have been removed by {guild}!')


# Class Links and Schedule
@bot.event
async def on_message(message):
    await bot.process_commands(message)  # allows commands to work with events
    if message.author == bot.user.id:
        return

    if message.content == '!help':
        content = '''
```css
Here are the list of commands that you can use:
```
```apache
!help
``` ```css
- shows the commands available.
``` ```apache
!bio
``` ```css
- shows the class link of Biology Class.
``` ```apache
!eap
``` ```css
 - shows the class link of English for Academic and Professional Purposes Class.
 ``` ```apache
!phy
``` ```css
- shows the class link of Physics Class.
``` ```apache
!entrep
``` ```css
- shows the class link of Entrepreneurship Class.
``` ```apache
!hr
``` ```css
- shows the class link for the Homeroom Class.
``` ```apache
!guidance
``` ```css
- shows the class link for the Guidance Class.
``` ```apache
!essfb
``` ```css
- shows the Official Facebook page of ESS. 
``` ```apache
!ess
``` ```css
- shows the Official Website of ESS.
``` ```apache
!guess
``` ```css
- play a guessing game!
``` ```apache
!sched
``` ```css
- shows the class schedule.
``` ```apache
!mega
``` ```css
- shows the file hosting site "MEGA"
``` ```apache
!gd
``` ```css
- shows the file hosting site "GOOGLE DRIVE"
``` ```apache
!db
``` ```css
- shows the file hosting site "DROPBOX"
``` ```apache
!md
``` ```css
- shows the file hosting site "MICROSOFT ONEDRIVE"
``` ```apache
!pb
``` ```css
- shows the website "PASTEBIN" where you can store notes.
``` ```apache
!git
``` ```css
- shows the official GitHub Repository of our Discord Bot.
```

        '''.format(message)
        await message.channel.send(content)

    if message.content == '!bio':
        content = f'{text} https://ess-edu-ph.zoom.us/j/87956674727%22'.format(message)
        await message.channel.send(content)

    if message.content == '!eap':
        content = f"{text1} https://ess-edu-ph.zoom.us/j/82906848571%22".format(message)
        await message.channel.send(content)

    if message.content == '!phy':
        content = f"{text2} https://ess-edu-ph.zoom.us/j/82364390272%22".format(message)
        await message.channel.send(content)

    if message.content == '!entrep':
        content = f"{text3} https://ess-edu-ph.zoom.us/j/84437506333%22".format(message)
        await message.channel.send(content)

    if message.content == '!hr':
        content = f'{text4} https://ess-edu-ph.zoom.us/j/98918318531'.format(message)
        await message.channel.send(content)

    if message.content == '!guidance':
        content = f'{text5} https://ess-edu-ph.zoom.us/j/99401621887'.format(message)
        await message.channel.send(content)

    if message.content == '!sched':
        content = f'{text6} https://ibb.co/bQccQTQ'.format(message)
        await message.channel.send(content)

    if message.content == '!essfb':
        content = f'{text7} https://www.facebook.com/elizabethsetonschool'.format(message)
        await message.channel.send(content)

    if message.content == '!ess':
        content = f'{text8} https://www.ess.edu.ph/'.format(message)
        await message.channel.send(content)

    if message.content == '!mega':
        content = f'{text9} https://mega.nz/login'.format(message)
        await message.channel.send(content)

    if message.content == '!gd':
        content = f'{text10} https://drive.google.com/'.format(message)
        await message.channel.send(content)

    if message.content == '!db':
        content = f'{text11} https://www.dropbox.com/login'.format(message)
        await message.channel.send(content)

    if message.content == '!md':
        content = f"{text12} https://onedrive.live.com/about/en-us/signin/".format(message)
        await message.channel.send(content)

    if message.content == '!pb':
        content = f'{text13} https://pastebin.pl/'.format(message)
        await message.channel.send(content)

    if message.content == '!git':
        content = f'{text14} https://github.com/KumikoNyan/ESS-Elizabeth-Seton-School-Bot'.format(message)
        await message.channel.send(content)

    # Easter Eggs

    if message.content == '!hello':  # Hello!
        content = 'Hello! {0.author.mention}'.format(message)
        await message.channel.send(content)

    if message.content == '!gay':  # kumiko and reina gay
        content = f'https://media1.tenor.com/images/bcd39f94b6e5e78b25bce85eb37c4b4a/tenor.gif?itemid=7347112'.format(
            message)
        await message.channel.send(content)

    if message.content == '!noice':  # noice
        content = f'https://media1.tenor.com/images/bcb961b67dc5ec34381372494c85c8fe/tenor.gif?itemid=8843762'.format(
            message)
        await message.channel.send(content)

    if message.content == '!fckshit':  # jamie fox fucking shit
        content = f'https://media1.tenor.com/images/05472297e9c5285b0b7ad18496ce6257/tenor.gif?itemid=18959222'.format(
            message)
        await message.channel.send(content)

    if message.content == '!rickroll':  # rickroll
        content = f'https://media1.tenor.com/images/8c409e6f39acc1bd796e8031747f19ad/tenor.gif?itemid=17029825'.format(
            message)
        await message.channel.send(content)

    # This is a simple code that will compliment you

    if message.content == '!Compliment':
        msg = await message.channel.send("You're bad!")
        await asyncio.sleep(1.0)
        await msg.edit(content='Just joking, you are good!')


# Extra Functionality (hello, ping, etc...)
# ping in ms (Conversion is 1s = 1000ms)
@bot.command()
async def ping(ctx):
    await ctx.send(f'Current latency is **{round(bot.latency * 1000)}ms**')


# clears text (default value is set to 5)
@bot.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


# Test your luck game  - made by me!
@bot.command(aliases=['8Ball', '8', 'EightBall'])
async def _8Ball(ctx, *, question):
    responses = ["It is certain.",
                 "It is decidedly so.",
                 "Without a doubt.",
                 "Yes - definitely.",
                 "You may rely on it.",
                 "As I see it, yes.",
                 "Most likely.",
                 "Outlook good.",
                 "Yes.",
                 "Signs point to yes.",
                 "Reply hazy, try again.",
                 "Ask again later.",
                 "Better not tell you now.",
                 "Cannot predict now.",
                 "Concentrate and ask again.",
                 "Don't count on it.",
                 "My reply is no.",
                 "My sources say no.",
                 "Outlook not so good.",
                 "Very doubtful."]
    await ctx.send(f'**Question:** {question}\n**Answer:** {random.choice(responses)}')

bot.run(token)
