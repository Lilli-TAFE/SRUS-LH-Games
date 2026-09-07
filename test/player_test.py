import unittest
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
        self.assertEqual(str(bob), "Player ID: id123, Player Name: Bob Smith")

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



if __name__ == '__main__':
    unittest.main()