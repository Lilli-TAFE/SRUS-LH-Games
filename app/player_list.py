from app.player import Player
from app.player_node import PlayerNode


class PlayerList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        self._is_empty = self.size == 0

    def push_head(self, player: Player):
        if self._is_empty:
            self._head = PlayerNode(player)
        else:
            old_head = self._head
            self._head = PlayerNode(player)
            self._head.set_next(old_head)
            old_head.set_prev(self._head)
