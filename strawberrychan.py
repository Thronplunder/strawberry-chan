import discord
import logging
from discord.ext.commands import Bot

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

token = open('token.txt', 'r').read()

print(token)

strawberrychan = Bot(';')


#@strawberrychan.event
#async def on_ready():
#    print("logged in as {0.user}".format(strawberrychan))


#@strawberrychan.event
#async def on_message(message):
#    if message.author == strawberrychan.user:
#        return
#    else:
#        print("{0.author} send the following: {0.content}".format(message))


@strawberrychan.command('queue')
async def queue(ctx):
    await ctx.send("Queued!")


strawberrychan.run(token)
