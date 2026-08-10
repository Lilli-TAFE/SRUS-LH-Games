class Player:
    def __init__(self, uniqueid: str, playername: str):
        self.uniqueid = uniqueid
        self.playername = playername

    def uid(self):
        return self.uniqueid

    def name(self):
        return self.playername

    def __str__(self):
        return "" + self.uniqueid + ", " + self.playername
