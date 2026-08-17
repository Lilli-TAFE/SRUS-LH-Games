from app.player import Player

class PlayerNode:

    def __init__(self, player: Player):
        self._player = player
        self._next = None
        self._prev = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev):
        self._prev = prev

    @property
    def get_player(self):
        return self._player

    @property
    def key(self):
        return self._player.uid

    def __str__(self):
        node_string = "Node: " + str(self._player)
        return node_string


