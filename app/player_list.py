from app.player import Player
from app.player_node import PlayerNode


class PlayerList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.is_empty = self.size == 0

    def push_head(self, player: Player):
        if self.is_empty:
            self.head = PlayerNode(player)
        else:
            old_head = self.head
            self.head = PlayerNode(player)
            self.head.set_next(old_head)
            old_head.set_prev(self.head)
