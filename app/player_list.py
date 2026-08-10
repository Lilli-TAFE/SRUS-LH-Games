from app.player import Player
from app.player_node import PlayerNode


class PlayerList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.is_empty = self.head is None and self.tail is None

    def push_head(self, player: Player):
        if self.is_empty:
            self.head = PlayerNode(player)
        else:
            old_head = self.head
            self.head = PlayerNode(player)
            self.head.set_next(old_head)
            old_head.set_prev(self.head)
