import unittest

from app.player_hash_map import PlayerHashMap
from app.player import Player

class PlayerHashMapTest(unittest.TestCase):

    def test_empty_list_size(self):
        list = PlayerHashMap()
        self.assertEqual(len(list), 0)

    def test_add_player_to_empty_list(self):
        list = PlayerHashMap()
        list["ID487"] = "Bobby Brown"
        self.assertIsInstance(list["ID487"], Player)
        self.assertEqual(list["ID487"], Player("ID487", "Bobby Brown"))

    def test_add_player_to_populated_list(self):
        pass

    def test_find_player_in_list(self):
        pass

    def test_remove_player_from_list(self):
        pass

    def test_list_size(self):
        pass
