class playerQueue:
    def __init__(self):
        self.players = []

    def addPlayer(self, playerid):
        self.players.append(playerid)

    def emptyQueue(self):
        del self.players[:]

    def getQueueLength(self):
        return len(self.players)

    def getPlayers(self):
        return self.players

    def removePlayer(self, id):
        self.players.remove(id)
