import discord
import logging
from discord.ext.commands import Bot
import playerqueue

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

token = open('token.txt', 'r').read()


class strawberrychan(Bot):
    def __init__(self, prefix):
        self.queue = playerqueue.playerQueue()
        Bot.__init__(self, prefix, status = discord.Status.invisible)

    def addplayer(self, playerid):
        self.queue.addplayer(playerid)
        if self.queue.getqueuelength() == 10:
            self.queue.emptyqueue()

    def getPlayerCountString(self):
        return "{0}/10 Players in queue".format(self.queue.getQueueLength())

    def generatePingAllPlayers(self):
        pingString = ""
        for player in self.queue.getPlayers():
            pingString = pingString + "<@{0.id}>, ".format(player)
        return pingString

    def generateCurrentQueue(self):
        players = ""
        numPlayers = len(self.queue.getPlayers())
        if numPlayers == 0:
            messageString = "Queue is Empty! Where are the players?"
        else:
            for player in self.queue.getPlayers():
                players = players + player.name + "\n"
            messageString = "__Current Queue: ({0}/10)__ \n {1}".format(numPlayers, players)
        return messageString


strawberryclient = strawberrychan(';')


@strawberryclient.command('queue')
async def queue(ctx):
    author = ctx.message.author
    if author in ctx.bot.queue.getPlayers():
        await ctx.send("You are already in the Queue!")
        return
    ctx.bot.queue.addPlayer(ctx.message.author)
    await ctx.send("Queued!\n\n " + ctx.bot.generateCurrentQueue())

    if ctx.bot.queue.getQueueLength() == 10:
        await ctx.send("Queue is full! " + ctx.bot.generatePingAllPlayers() + "Someone go make Lobby and join, i cant do that yet!")
        ctx.bot.queue.emptyQueue()


@strawberryclient.event
async def on_ready():
    print("ready")
    await strawberryclient.change_presence(status=discord.Status.invisible)

@strawberryclient.command('unqueue')
async def unqueue(ctx):
    author = ctx.message.author
    if author not in ctx.bot.queue.getPlayers():
        await ctx.send("You need to queue first!")
        return
    ctx.bot.queue.removePlayer(ctx.message.author)
    await ctx.send("Unqueued! \n\n" + ctx.bot.generateCurrentQueue())


@strawberryclient.command('list')
async def printQueue(ctx):
    await ctx.send(ctx.bot.generateCurrentQueue())


@strawberryclient.command('clear')
async def clearQueue(ctx):
    if ctx.bot.queue.getQueueLength() == 0:
        await ctx.send("Queue is already empty!")
        return
    ctx.bot.queue.emptyQueue()
    await ctx.send("Queue was cleared!")


strawberryclient.run(token)
