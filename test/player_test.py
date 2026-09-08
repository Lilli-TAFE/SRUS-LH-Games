import unittest
import random
from app.player import Player


class PlayerTest(unittest.TestCase):
    def test_player_uid_and_name(self):
        bob = Player("id123", "Bob Smith")
        # test the uid is set correctly
        self.assertEqual(bob.uid, "id123")
        # test the name is set correctly
        self.assertEqual(bob.name, "Bob Smith")

    def test_player_str(self):
        bob = Player("id123", "Bob Smith")
        # test the string is displaying correctly
        self.assertEqual(str(bob), "Player ID: id123, Player Name: Bob Smith, Player score: 0")

    def test_sort_players(self):
        # changed to match my implementation
        players = [Player("01", "Alice", player_score=10), Player("02", "Bob", player_score=5), Player("03", "Charlie", player_score=15)]
        # note: ensure initialization code is valid for **your** implementation.
        # For example, is your parameter called uid? is the first parameter name?

        # do **not** change the following code:
        sorted_players = sorted(players)

        # players must be sorted by score as shown here:
        # changed to match my implementation
        manually_sorted_players = [Player("02", "Bob", player_score=5), Player("01", "Alice", player_score=10), Player("03", "Charlie", player_score=15)]

        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_players_can_be_compared_by_score(self):
        # note: ensure initialization code is valid for **your** implementation
        alice = Player("01", "Alice", player_score=10)
        bob = Player("02", "Bob", player_score=5)

        # Add the appropriate expression to the following assert test
        self.assertLess(bob, alice)

    def test_sort_3_players_custom_algorithm(self):
        # Set up same as test_sort_players
        players = [Player("01", "Alice", player_score=10), Player("02", "Bob", player_score=5), Player("03", "Charlie", player_score=15)]

        sorted_players = Player.sort_players(players)
        manually_sorted_players = [Player("03", "Charlie", player_score=15), Player("01", "Alice", player_score=10), Player("02", "Bob", player_score=5)]

        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_sort_1000_players_custom_algorithm(self):
        players = [Player(f"{i:03}", f"Player {i}", player_score=random.randint(0, 1000)) for i in range(1000)]
        # builtin method vs custom
        self.assertEqual(sorted(players, reverse=True), Player.sort_players(players))



if __name__ == '__main__':
    unittest.main()