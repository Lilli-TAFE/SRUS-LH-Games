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

    def test_add_multiple_players(self):
        list = PlayerHashMap()
        players = [
                    ["ID123", "Bob Smith"],
                    ["ID234", "Jane Doe"],
                    ["ID456", "Mickey Mouse"],
                    ["ID567", "Donald Duck"],
                ]

        for player in players:
            list[player[0]] = player[1]

        for player in players:
            self.assertEqual(Player(player[0], player[1]), list[player[0]])


    def test_find_player_in_list(self):
        list = PlayerHashMap()
        players = [
                    ["ID123", "Bob Smith"],
                    ["ID234", "Jane Doe"],
                    ["ID456", "Mickey Mouse"],
                    ["ID567", "Donald Duck"],
                ]

        for player in players:
            list[player[0]] = player[1]

        self.assertEqual(list["ID234"], Player("ID234", "Jane Doe"))

    def test_remove_player_from_list(self):
        list = PlayerHashMap()
        players = [
                    ["ID123", "Bob Smith"],
                    ["ID234", "Jane Doe"],
                    ["ID456", "Mickey Mouse"],
                    ["ID567", "Donald Duck"],
                ]

        for player in players:
            list[player[0]] = player[1]

        self.assertEqual(len(list), 4)
        del list["ID456"]
        self.assertEqual(len(list), 3)
        self.assertIsNone(list["ID456"])

    def test_list_size(self):
        list = PlayerHashMap()
        players = [
                    ["ID123", "Bob Smith"],
                    ["ID234", "Jane Doe"],
                    ["ID456", "Mickey Mouse"],
                    ["ID567", "Donald Duck"],
                ]

        for player in players:
            list[player[0]] = player[1]

        print("List displayed: ")
        print(list.display())
        self.assertEqual(len(list), 4)
        
