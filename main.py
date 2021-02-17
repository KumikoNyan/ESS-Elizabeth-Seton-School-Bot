import discord
import random
import asyncio

client = discord.Client()

TOKEN = 'Your Token Here!'

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

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!help':
        msg = '''
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
```
        '''.format(message)
        await message.channel.send(msg)

    if message.content == '!hello':
        msg = ' こんにちはマスター！{0.author.mention}'.format(message)
        await message.channel.send(msg)

    if message.content == '!bio':
        msg = f'{text} https://ess-edu-ph.zoom.us/j/87956674727%22'.format(message)
        await message.channel.send(msg)

    if message.content == '!eap':
        msg = f"{text1} https://ess-edu-ph.zoom.us/j/82906848571%22".format(message)
        await message.channel.send(msg)

    if message.content == '!phy':
        msg = f"{text2} https://ess-edu-ph.zoom.us/j/82364390272%22".format(message)
        await message.channel.send(msg)

    if message.content == '!entrep':
        msg = f"{text3} https://ess-edu-ph.zoom.us/j/84437506333%22".format(message)
        await message.channel.send(msg)

    if message.content == '!hr':
        msg = f'{text4} https://ess-edu-ph.zoom.us/j/98918318531'.format(message)
        await message.channel.send(msg)

    if message.content == '!guidance':
        msg = f'{text5} https://ess-edu-ph.zoom.us/j/99401621887'.format(message)
        await message.channel.send(msg)

    if message.content == '!sched':
        msg = f'{text6} https://ibb.co/bQccQTQ'.format(message)
        await message.channel.send(msg)

    if message.content == '!essfb':
        msg = f'{text7} https://www.facebook.com/elizabethsetonschool'.format(message)
        await message.channel.send(msg)

    if message.content == '!ess':
        msg = f'{text8} https://www.ess.edu.ph/'.format(message)
        await message.channel.send(msg)

    if message.content == '!mega':
        msg = f'{text9} https://mega.nz/login'.format(message)
        await message.channel.send(msg)

    if message.content == '!gd':
        msg = f'{text10} https://drive.google.com/'.format(message)
        await message.channel.send(msg)

    if message.content == '!db':
        msg = f'{text11} https://www.dropbox.com/login'.format(message)
        await message.channel.send(msg)

    if message.content == '!md':
        msg = f'{text12} https://onedrive.live.com/about/en-us/signin/'.format(message)
        await message.channel.send(msg)

    if message.content == '!pb':
        msg = f'{text13} https://pastebin.pl/'.format(message)
        await message.channel.send(msg)

# Guessing Game
    if message.content == '!guess':
        await message.channel.send('Guess a number between 1 and 10.')

        def is_correct(m):
            return m.author == message.author and m.content.isdigit()
        answer = random.randint(1, 10)

        try:
            guess = await client.wait_for('message', check=is_correct, timeout=5.0)
        except asyncio.TimeoutError:
            return await message.channel.send('Sorry, you suck! {}.'.format(answer))

        if int(guess.content) == answer:
            await message.channel.send('You are right!')
        else:
            await message.channel.send('You still suck. It is actually {}.'.format(answer))

@client.event
async def on_ready():
    print('beep boop')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
