import unittest
from app.player import Player


class PlayerTest(unittest.TestCase):
    def test_player_uid(self):
        bob = Player("id123", "Bob Smith")
        self.assertEqual(bob.uid(), "id123")

    def test_player_name(self):
        bob = Player("id123", "Bob Smith")
        self.assertEqual(bob.name(), "Bob Smith")

if __name__ == '__main__':
    unittest.main()
