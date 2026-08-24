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


if __name__ == '__main__':
    unittest.main()