from app.player import Player
from app.player_node import PlayerNode


class PlayerList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    @property
    def size(self):
        return self._size

    @property
    def is_empty(self):
        return self.size == 0

    
    def push_head(self, player: Player):

        if self.is_empty:
            self._head = PlayerNode(player)
            self._tail = self._head
        else:
            self._head = PlayerNode(player, self._head)
            self._head.next.prev = self._head

        self._size += 1
