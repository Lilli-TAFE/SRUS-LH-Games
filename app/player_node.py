from app.player import Player

class PlayerNode:

    def __init__(self, player: Player, next = None, prev = None):
        self._player = player
        self._next = next
        self._prev = prev

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next: PlayerNode):
        self._next = next

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev: PlayerNode):
        self._prev = prev

    @property
    def player(self):
        return self._player

    @property
    def key(self):
        return self._player.uid

    def __str__(self):
        node_string = "Node: " + str(self._player)
        return node_string


