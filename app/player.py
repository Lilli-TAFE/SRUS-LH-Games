class Player:
    def __init__(self, uniqueId: str, playerName: str):
        self.uniqueId = uniqueId
        self.playerName = playerName

    def uid(self):
        return self.uniqueId

    def name(self):
        return self.playerName

    def __str__(self):
        return "" + self.uniqueId + ", " + self.playerName
