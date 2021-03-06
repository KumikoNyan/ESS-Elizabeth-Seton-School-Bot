import discord
import asyncio
import random
import pekofy as peko
import replies
# import os - use this if you want to use the for filename method instead of the bot.load_extension
import datetime
from discord.ext import commands, tasks
from itertools import cycle
from discord.ext.commands import CommandNotFound

token = 'token'

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
toDoDB = []  # empty list for storing stuffs lol
# bot = discord.Client()
bot = commands.Bot(command_prefix='!', intents=intents)
# bot.load_extension('cogs.Todo')  # load the Todo feature with timers

# Variables needed for the formatted strings
status = cycle(['!help', '@KumikoNyan', '@MoeFAX', '@Jinrooo', 'Destiny 2', 'Fallout 4', 'Skyrim SE', 'I love you!'])
text = 'This is **Biology Class**:\n '
text1 = 'This is **English for Academic and Professional Purposes Class**:\n '
text2 = 'This is **Physics Class**:\n '
text3 = 'This is **Entrepreneurship Class**:\n '
text4 = 'This is **Homeroom**:\n '
text5 = 'This is **Guidance**:\n '
text6 = 'Here is your class schedule for this term. Enjoy Learning!\n '
text7 = "Stay updated with Elizabeth Seton School's Facebook Page:\n "
text8 = "Check out the official website of Elizabeth Seton School:\n "
text9 = "**MEGA**:\n "
text10 = "**GOOGLE DRIVE**:\n "
text11 = "**DROPBOX**:\n "
text12 = "**MICROSOFT ONEDRIVE**:\n "
text13 = "**PASTEBIN**:\n "
text14 = "**ESS BOT OFFICIAL GITHUB REPOSITORY:**\n"
text15 = """
:alarm_clock: **How to use the Reminder?** :alarm_clock:
```'$remind/remindme/remind_me [Time] [Your Reminder].'
Time can be in:
d - days\nh - hours\nm - minutes\ns - seconds
'!helpr' - shows this menu.
example: !remindme 30s Check the stove.\nby @KumikoNyan```"""


# Pekofy Bot Functions
def reply_chance(percent):
    return random.randint(0, 100) <= percent

# ToDo List Functions by @KumikoNyan
def channelDBManager(channel):
    channelExists = False
    for db in toDoDB:
        if db[0] == channel:
            channelExists = True
            currentDB = db[1]

    if not channelExists:
        toDoDB.append([channel, []])
        for db in toDoDB:
            if db[0] == channel:
                currentDB = db[1]
    try:
        return currentDB
    except:
        print("channeldbmanager fatal fail - exiting")
        exit()


def newToDo(desc, channel):
    db = channelDBManager(channel)
    status = True
    tempTodo = [desc, status]
    db.append(tempTodo)


def doneToDo(id, channel):
    db = channelDBManager(channel)
    i = 0
    success = False
    for todo in db:
        i += 1
        if i == id:
            success = True
            tempI = i - 1
            db.remove(db[tempI])
    return success


def listToDo(channel):
    db = channelDBManager(channel)
    id = 0
    returnList = []
    for todo in db:
        temptodo = []
        for i in todo:
            temptodo.append(i)
        id += 1
        temptodo.insert(0, id)
        returnList.append(temptodo)
    return returnList


# Checks if the Bot is ready
@bot.event
async def on_ready():
    change_status.start()  # will change the status or activity of the bot given the parameters
    print('--------------------------')
    print('The Bot is ready!')
    print(bot.user.name)
    print(bot.user.id)
    print('--------------------------')


# This godsend error handler to avoid "COMMAND NOT FOUND" false positive.
@bot.event
async def on_command_error(ctx, error):  # you shouldn't remove ctx or the run will get piled up with 'CommandNotFound'
    if isinstance(error, CommandNotFound):
        return
    raise error


# Logging
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
        await message.channel.purge(limit=2)
        content = """
        
:mechanical_arm: **List of Commands:** :mechanical_leg:
```'!help' - shows this menu.\n'!commands' - DMs this menu.\n'!bio' - shows the class link for the Biology class.
'!eap' - shows the class link for EAP class.\n'!phy' - shows the class link for Physics class.
'!entrep' - shows the class link for Entrepreneurship class.\n'!hr' - shows the class link for Homeroom.
'!guidance' - shows the class link for Guidance class.\n'!sched' - shows the current schedule for the term.```

:school: **ELIZABETH SETON SCHOOL INFORMATION:** :school_satchel:
```'!essfb' - shows the official Facebook page of Elizabeth Seton School.
'!ess' - shows the official website of Elizabeth Seton School.```

:alarm_clock: **How to use the Reminder?** :alarm_clock:
```'!remind/remindme/remind_me [Time] [Your Reminder].'
Time can be in:
d - days\nh - hours\nm - minutes\ns - seconds
'!helpr' - shows this menu.
example: !remindme 30s Check the stove.\nby @KumikoNyan```

:question: **How to use the Todo List?** :question:
```'!todo' - Show the current todo list.\n'!add [TODO]' - Add a new todo.\n'!done [ID]' - Mark a todo done (delete).
'!helpt' - Show this menu.\nby @KumikoNyan```

:file_folder: **File Hosting Sites and More!** :open_file_folder:
```'!mega' - shows the MEGA file hosting site.\n'!gd' - shows Google Drive.\n'!db' - shows Dropbox.
'!md' - shows Microsoft OneDrive.\n'!pb' - shows the reliable Paste Bin!
'!git' - shows the official GitHub repository of the ESS-Bot for Discord!```

:ok_hand: **Extra Commands:** :ok_hand:
```'!ping' - to check the current latency.\n'!clear [value]' - clears certain amount of messages (limit is 10).
'!8 [Question]' - try out our new 8 Ball Magic Game!```


        """.format(message)
        await message.channel.send(content)

    if message.content == '!bio':
        await message.channel.purge(limit=1)
        content = f"{text}".format(message)
        await message.channel.send(content)

    if message.content == '!eap':
        await message.channel.purge(limit=1)
        content = f"{text1} ".format(message)
        await message.channel.send(content)

    if message.content == '!phy':
        await message.channel.purge(limit=1)
        content = f"{text2}".format(message)
        await message.channel.send(content)

    if message.content == '!entrep':
        await message.channel.purge(limit=1)
        content = f"{text3}".format(message)
        await message.channel.send(content)

    if message.content == '!hr':
        await message.channel.purge(limit=1)
        content = f"{text4}".format(message)
        await message.channel.send(content)

    if message.content == '!guidance':
        await message.channel.purge(limit=1)
        content = f"{text5}".format(message)
        await message.channel.send(content)

    if message.content == '!sched':
        await message.channel.purge(limit=1)
        content = f"{text6}".format(message)
        await message.channel.send(content)

    if message.content == '!essfb':
        await message.channel.purge(limit=1)
        content = f"{text7}".format(message)
        await message.channel.send(content)

    if message.content == '!ess':
        await message.channel.purge(limit=1)
        content = f"{text8}".format(message)
        await message.channel.send(content)

    if message.content == '!mega':
        await message.channel.purge(limit=1)
        content = f'{text9} https://mega.nz/login'.format(message)
        await message.channel.send(content)

    if message.content == '!gd':
        await message.channel.purge(limit=1)
        content = f'{text10} https://drive.google.com/'.format(message)
        await message.channel.send(content)

    if message.content == '!db':
        await message.channel.purge(limit=1)
        content = f'{text11} https://www.dropbox.com/login'.format(message)
        await message.channel.send(content)

    if message.content == '!md':
        await message.channel.purge(limit=1)
        content = f"{text12} https://onedrive.live.com/about/en-us/signin/".format(message)
        await message.channel.send(content)

    if message.content == '!pb':
        await message.channel.purge(limit=1)
        content = f'{text13} https://pastebin.pl/'.format(message)
        await message.channel.send(content)

    if message.content == '!git':
        await message.channel.purge(limit=1)
        content = f'{text14} https://github.com/KumikoNyan/ESS-Elizabeth-Seton-School-Bot'.format(message)
        await message.channel.send(content)

    if message.content == '!helpr':
        await message.channel.purge(limit=1)
        content = f'{text15}'.format(message)
        await message.channel.send(content)

# ----------------------------------------------------------------------------------
# Pekofy Bot thanks to @bemxio
# pain peko (not used regex for faster results)

    if message.content.lower() in ["pain", "pain.", "pain...", "pain peko", "pain peko."] and reply_chance(50):
        await message.channel.send(replies.pain_peko_reply)

    # hey moona
    if "moona" in message.content.lower() and "pekora" in message.content.lower() and reply_chance(25):
        await message.channel.send(replies.hey_moona_reply)

    # help command
    if message.content.startswith("!helpeko"):
        await message.channel.send(replies.helpeko)

    # pekofy command
    if message.content.startswith('!pekofy'):
        channel = message.channel

        if message.reference:
            reply = message.reference.resolved
        else:
            return

        if reply.author == bot.user:
            await message.channel.send(replies.found_myself)
            return

        reply = reply.content
        """
        try:
            reply = message.reference.resolved.content
        except AttributeError: # if no message.reference found
            reply = await channel.history(limit=2).flatten()
            reply = reply[1].content
        """
        reply = peko.pekofy(reply)

        # if it couldn't be pekofied, give a random pekora clip
        if reply in ["NOTHING_CHANGED", "NO_LETTER"]:
            reply = random.choice(replies.nothing_changed_reply_list)

        await message.channel.send(reply)

    # insulting people
    if message.content.lower() == "insult me peko":
        await message.channel.send(random.choice(replies.insults))

    if message.content == "!pekopasta":  # easter egg
        await message.channel.send(replies.cursed_pekopasta)

    # rating reactions
    if message.reference:  # if the message is a reply
        if message.reference.resolved.author == bot.user:
            if "good bot" in message.content.lower():
                await message.channel.send(random.choice(replies.thanks))
            if "bad bot" in message.content.lower():
                await message.channel.send(random.choice(replies.sorrys))
            if "cute bot" in message.content.lower():
                await message.channel.send(random.choice(replies.cutes))
            if message.content.lower() in ["i love you", "love you", "love", "i love you peko", "love you peko",
                                           "love peko"]:
                await message.channel.send(random.choice(replies.loves))
# --------------------------------------------------------------------------------


# Easter Eggs (Not really important but hey)
    if message.content == '!hello':  # Hello!
        content = 'Hello! {0.author.mention}'.format(message)
        await message.channel.send(content)

    if message.content == '!gay':  # Kumiko and Reina
        content = f'https://media1.tenor.com/images/bcd39f94b6e5e78b25bce85eb37c4b4a/tenor.gif?itemid=7347112'.format(
            message)
        await message.channel.send(content)

    if message.content == '!noice':  # NOICE
        content = f'https://media1.tenor.com/images/bcb961b67dc5ec34381372494c85c8fe/tenor.gif?itemid=8843762'.format(
            message)
        await message.channel.send(content)

    if message.content == '!fckshit':  # Jamie Fox
        content = f'https://media1.tenor.com/images/05472297e9c5285b0b7ad18496ce6257/tenor.gif?itemid=18959222'.format(
            message)
        await message.channel.send(content)

    if message.content == '!rickroll':  # Rick Roll
        content = f'https://media1.tenor.com/images/8c409e6f39acc1bd796e8031747f19ad/tenor.gif?itemid=17029825'.format(
            message)
        await message.channel.send(content)

    # This is a simple code that will compliment you - again not important but hey, why not?

    if message.content == '!Compliment':
        msg = await message.channel.send("You're bad!")
        await asyncio.sleep(1.0)
        await msg.edit(content='Just joking, you are good!')


# ------------------------------------------------------
# ToDo Event by @KumikoNyan
# !help for more command info about the ToDo function
# !todo to check your current todo list
# !add to add more stuffs to your list (lol?)
# !done (list number) (e.g. 1) to mark it as done
# ------------------------------------------------------

    channel = str(message.channel.id)

    command = str(message.content)
    if command.startswith("!"):

        print(toDoDB)

        if command.startswith("!add "):
            command = command.replace("!add ", "")
            if command == "":
                await message.author.send(":x: No ToDo entered.")
                print(":x: No ToDo entered.")
            newToDo(command, channel)
            await message.author.send(":white_check_mark: ToDo `" + command + "` added.")
            await message.channel.purge(limit=1)
            print(":white_check_mark: ToDo '" + command + "' added.")
        elif command == "!add":
            await message.author.send(":x: Usage: `!add [TODO]`")
            print(":x: Usage: `!add [TODO]`")

        elif command == "!todo":
            await message.channel.purge(limit=1)
            list = listToDo(channel)
            printline = ""
            for todo in list:
                printline = printline + "**[" + str(todo[0]) + "]** - " + str(todo[1]) + "\n"
            if printline == "":
                printline = ":metal: **No ToDo's!** :metal:"
            else:
                printline = ":pencil: **ToDo's:** :pencil:\n\n" + printline
            # await message.channel.send(printline)
            await message.author.send(printline)
            print(printline)

        elif command.startswith("!done "):
            command = command.replace("!done ", "")
            await message.channel.purge(limit=1)
            try:
                command = int(command)
            except:
                await message.author.send(':x: ID needs to be a number!')
                print(":x: ID needs to be a number!")
                return
            success = doneToDo(command, channel)
            if success:
                await message.author.send(':white_check_mark: ToDo done.')
                await message.delete()
                print(":white_check_mark: ToDo deleted")
            else:
                await message.author.send(':x: No ToDo with ID **' + str(command) + '**')
                print(':x: No ToDo with ID **' + str(command) + '**')
        elif command == "!done":
            await message.author.send(":x: Usage: `!done [ID]`")
            print(":x: Usage: `!done [ID]`")

        elif command == "!helpt":
            printline = "'!todo' - Show the current todo list.\n'!add [TODO]' - Add a new todo.\n'!done [ID]' - Mark a todo done (delete).\n'!helpt' - Show this menu.\nby @KumikoNyan"
            printline = ":question: **Help menu:** :question:\n" + "```" + printline + "```"
            await message.author.send(printline)
            await message.channel.purge(limit=1)
            print(printline)


# -------------------------------------------------
# Reminder by @KumikoNyan (Owner)
# $remind/remindme/remind_me [Time] [Your Reminder]
# Time can be in:
# d - days | h - hours | m - minutes | s - seconds
# $help - shows this menu.
# example: !remindme 30s Check the stove.
# -------------------------------------------------


@bot.command(case_insensitive=True, aliases=["remind", "remindme", "remind_me"])
@commands.bot_has_permissions(attach_files=True, embed_links=True)
async def reminder(ctx, time, *, reminder):
    await ctx.channel.purge(limit=1)
    print(time)
    print(reminder)
    user = ctx.message.author
    embed = discord.Embed(color=0x55a7f7, timestamp=datetime.datetime.utcnow())

    seconds = 0
    if reminder is None:
        embed.add_field(name='Warning',
                        value='Please specify what do you want me to remind you about.')  # Error message
    if time.lower().endswith("d"):
        seconds += int(time[:-1]) * 60 * 60 * 24
        counter = f"{seconds // 60 // 60 // 24} days"
    if time.lower().endswith("h"):
        seconds += int(time[:-1]) * 60 * 60
        counter = f"{seconds // 60 // 60} hours"
    elif time.lower().endswith("m"):
        seconds += int(time[:-1]) * 60
        counter = f"{seconds // 60} minutes"
    elif time.lower().endswith("s"):
        seconds += int(time[:-1])
        counter = f"{seconds} seconds"
    if seconds == 0:
        embed.add_field(name='Warning',
                            value='Please type !helpr for more information')
    elif seconds < 10:
        embed.add_field(name='Warning',
                            value='You have specified a too short duration!\nMinimum duration is 10 seconds.')
    elif seconds > 31536000:
        embed.add_field(name='Warning',
                            value='You have specified a too long duration!\nMaximum duration is 1 year.')
    else:
        await ctx.author.send(f"Alright {user.mention}, I will remind you about: ```{reminder}``` in **{counter}**.")
        await asyncio.sleep(seconds)
        await ctx.author.send(f"Hi {user.mention}, you asked me to remind you about: ```{reminder}``` **{counter}** ago.")
        return
    await ctx.send(embed=embed)


# Commands (NOT ALL ARE VISIBLE FOR USERS)


@bot.command(aliases=['helpc'])
async def commands(ctx):
    user = ctx.message.author
    await ctx.channel.purge(limit=1)
    await ctx.author.send(f"""

***Thank you {user.mention} for using Ina'nis bot! Here are the list of commands available!***

:mechanical_arm: **List of Commands:** :mechanical_leg:
```'!help' - shows this menu.\n'!commands' - DMs this menu.\n'!bio' - shows the class link for the Biology class.
'!eap' - shows the class link for EAP class.\n'!phy' - shows the class link for Physics class.
'!entrep' - shows the class link for Entrepreneurship class.\n'!hr' - shows the class link for Homeroom.
'!guidance' - shows the class link for Guidance class.\n'!sched' - shows the current schedule for the term.```

:school: **ELIZABETH SETON SCHOOL INFORMATION:** :school_satchel:
```'!essfb' - shows the official Facebook page of Elizabeth Seton School.
'!ess' - shows the official website of Elizabeth Seton School.```

:alarm_clock: **How to use the Reminder?** :alarm_clock:
```'!remind/remindme/remind_me [Time] [Your Reminder].'
Time can be in:
d - days\nh - hours\nm - minutes\ns - seconds
'!helpr' - shows this menu.
example: !remindme 30s Check the stove.\nby @KumikoNyan```

:question: **How to use the Todo List?** :question:
```'!todo' - Show the current todo list.\n'!add [TODO]' - Add a new todo.\n'!done [ID]' - Mark a todo done (delete).
'!helpt' - Show this menu.\nby @KumikoNyan```

:file_folder: **File Hosting Sites and More!** :open_file_folder:
```'!mega' - shows the MEGA file hosting site.\n'!gd' - shows Google Drive.\n'!db' - shows Dropbox.
'!md' - shows Microsoft OneDrive.\n'!pb' - shows the reliable Paste Bin!
'!git' - shows the official GitHub repository of the ESS-Bot for Discord!```

:ok_hand: **Extra Commands:** :ok_hand:
```'!ping' - to check the current latency.\n'!clear [value]' - clears certain amount of messages (limit is 10).
'!8 [Question]' - try out our new 8 Ball Magic Game!```""")


@bot.command()
async def ping(ctx):
    await ctx.send(f'Current latency is **{round(bot.latency * 1000)}ms**')


# clears text (default value is set to 10)
@bot.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)


# loads cogs - won't do anything unless you have cogs/extensions.
@bot.command()
async def load(extension):
    bot.load_extension(f'cogs.{extension}')


# unloads cogs - same for load
@bot.command()
async def unload(extension):
    bot.unload_extension(f'cogs.{extension}')


# reloads cogs - same for load
@bot.command()
async def reload(extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')


# For thos who want to use this method
# for filename in os.listdir('Your Directory'):
#    if filename.endswith('.py'):
#       bot.load_extension(f'cogs.{filename[:-3]}')


# Test your luck game  - made by @KumikoNyan
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


# Changes the status of the bot
@tasks.loop(seconds=10)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))

bot.run(token)
