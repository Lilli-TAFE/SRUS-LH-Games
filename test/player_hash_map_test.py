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

    def test_change_player_name(self):
        list = PlayerHashMap()
        players = [
            ["ID123", "Bob Smith"],
            ["ID234", "Jane Doe"],
            ["ID456", "Mickey Mouse"],
            ["ID567", "Donald Duck"],
        ]

        for player in players:
            list[player[0]] = player[1]

        list["ID567"] = "Big Bird"
        self.assertEqual(list["ID567"], Player("ID567", "Big Bird"))

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

        self.assertEqual(len(list), 4)

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

    def test_saturated_list(self):
        list = PlayerHashMap()
        players = [
            ["ID123", "Bob Smith"],
            ["ID234", "Jane Doe"],
            ["ID456", "Mickey Mouse"],
            ["ID567", "Donald Duck"],
            ["ID987", "Bob Johnson"],
            ["ID877", "Jane Fredson"],
            ["ID765", "Minnie Mouse"],
            ["ID674", "Donald Quack"],
            ["ID543", "Bob Brown"],
            ["ID777", "Jane White"],
            ["ID944", "Green Goblin"],
            ["ID321", "Big Bird"],
            ["ID111", "Blue Bear"],
            ["ID222", "Red Dog"],
            ["ID333", "Jeff Asleep"],
            ["ID444", "The Wiggles"],
            ["ID445", "Spiderman"],
            ["ID667", "Clark Kent"],
            ["ID878", "Mary Jane"],
            ["ID560", "Batman"],
            ["ID087", "Robin"],
            ["ID824", "The Joker"],
            ["ID998", "Anonymous"],
            ["ID563", "Ella Fitzgerald"],
            ["ID485", "Billy Joel"],
            ["ID687", "Bob McFerrin"],
            ["ID898", "Yo-Yo Ma"],
            ["ID590", "Ghost"],
            ["ID097", "Mastodon"],
            ["ID894", "Machine Head"],
            ["ID908", "Metallica"],
            ["ID503", "Mudvayne"],
        ]

        for player in players:
            list[player[0]] = player[1]

        # To manually check distribution of players
        print("List display: ")
        print(list.display())
        for player_list in list._player_hash_array:
            # Setting a tolerance that the length of each player list
            # in the array should be less than twice the average number
            # of players in each list. This is somewhat arbitrarily
            # chosen and could be changed.
            self.assertLess(player_list.size, (len(list) / 10) * 2)
        # Test length
        self.assertEqual(len(list), len(players))
        # Test remove
        del list["ID590"]
        self.assertIsNone(list["ID590"])
