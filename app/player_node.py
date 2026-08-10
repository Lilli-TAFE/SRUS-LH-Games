from app.player import Player

class PlayerNode:

    def __init__(self, player: Player):
        self.player = player
        self.next = None
        self.prev = None

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

    def get_prev(self):
        return self.prev

    def set_prev(self, prev):
        self.prev = prev

    def get_player(self):
        return self.player

    def key(self):
        return self.player.uid()

    def __str__(self):
        node_string = "Node key: " + str(self.player)
        return node_string


