import unittest

from app.player import Player
from app.player_list import PlayerList


class PlayerListTest(unittest.TestCase):

    def test_add_node_to_empty_list(self):
        list = PlayerList()
        player = Player("ID123", "Bob Smith")
        list.push_head(player)
        self.assertEqual(list.head.get_player(), player)

    def test_add_node_to_populated_list(self):
        pass