# This is the 'Todo List' feature that our bot currently uses.
# You can use the optional one if you want timers for every list or to be set.
# If you want the other 'ToDo' check it under the cogs folder.
# Yours truly, @KumikoNyan

import discord
import asyncio
from discord.ext import commands
toDoDB = []
bot = commands.Bot(command_prefix='!')
token = 'token'


# ToDo List Functions by @KumikoNyan (Owner)
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

# ------------------------------------------------------
# ToDo Event by @KumikoNyan (Owner)
# -help for more command info about the ToDo function
# -todo to check your current todo list
# -add to add more stuffs to your list (lol?)
# -done (list number) (e.g. 1) to mark it as done
# ------------------------------------------------------


@bot.event
async def on_message(message):
    await bot.process_commands(message)  # use this if you have commands in your code
    if message.author == bot.user.id:
        return

    channel = str(message.channel.id)

    command = str(message.content)

    if command.startswith("-"):

        print(toDoDB)

        if command.startswith("-add "):
            command = command.replace("-add ", "")
            if command == "":
                await message.channel.send(":x: No ToDo entered.")
                print(":x: No ToDo entered.")
            newToDo(command, channel)
            await message.channel.send(":white_check_mark: ToDo `" + command + "` added.")
            print(":white_check_mark: ToDo '" + command + "' added.")
        elif command == "-add":
            await message.channel.send(":x: Usage: `-add [TODO]`")
            print(":x: Usage: `-add [TODO]`")

        elif command == "-todo":
            list = listToDo(channel)
            printline = ""
            for todo in list:
                printline = printline + "**[" + str(todo[0]) + "]** - " + str(todo[1]) + "\n"
            if printline == "":
                printline = ":metal: **No ToDo's!** :metal:"
            else:
                printline = ":pencil: **ToDo's:** :pencil:\n\n" + printline
            await message.channel.send(printline)
            print(printline)

        elif command.startswith("-done "):
            command = command.replace("-done ", "")
            try:
                command = int(command)
            except:
                await message.channel.send(':x: ID needs to be a number!')
                print(":x: ID needs to be a number!")
                return
            success = doneToDo(command, channel)
            if success:
                await message.channel.send(':white_check_mark: ToDo done.')
                print(":white_check_mark: ToDo deleted")
            else:
                await message.channel.send(':x: No ToDo with ID **' + str(command) + '**')
                print(':x: No ToDo with ID **' + str(command) + '**')
        elif command == "-done":
            await message.channel.send(":x: Usage: `-done [ID]`")
            print(":x: Usage: `-done [ID]`")

        elif command == "-help":
            printline = "-todo' - Show the current todo list.\n'-add [TODO]' - Add a new todo.\n'-done [ID]' - Mark a todo done (delete).\n'-help' - Show this menu.\nby @KumikoNyan"
            printline = ":question: **Help menu:** :question:\n" + "```" + printline + "```"
            await message.channel.send(printline)
            print(printline)


@bot.event
async def on_ready():
    print('-----------------------------')
    print('Bot is now online.')
    print(bot.user.name)
    print(bot.user.id)
    print('-----------------------------')

bot.run(token)



