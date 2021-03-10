from discord.ext import commands
import pekofy as peko  # because i am gonna copy paste a lot of stuff
import replies
import discord
import random

bot = discord.Client()
token = 'token'
# keyphrase = '!pekofy'


def reply_chance(percent):
    return random.randint(0, 100) <= percent


@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Game(name=replies.status_content))


@bot.event
@commands.cooldown(1, 5, commands.BucketType.user)
async def on_message(message):
    if message.author == bot.user:
        return

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
            if message.content.lower() in ["i love you", "love you", "love", "i love you peko", "love you peko", "love peko"]:
                await message.channel.send(random.choice(replies.loves))

bot.run(token)