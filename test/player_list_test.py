import unittest

from app.player import Player
from app.player_list import PlayerList


class PlayerListTest(unittest.TestCase):

# HEAD TESTS
    def test_push_head_to_empty_list(self):
        list = PlayerList()
        firstPlayer = Player("ID123", "Bob Smith")
        list.push_head(firstPlayer)
        # test node correctly added
        self.assertEqual(list.head.player, firstPlayer)
        # test prev and next are correctly showing None
        self.assertIsNone(list.head.next)
        self.assertIsNone(list.head.prev)
        self.assertEqual(list.head, list.tail)
        

    def test_push_head_to_list_of_one(self):
        list = PlayerList()
        firstPlayer = Player("ID123", "Bob Smith")
        list.push_head(firstPlayer)
        secondPlayer = Player("ID234", "Jane Doe")
        list.push_head(secondPlayer)

        # test second node correctly added as the head including all 
        # references correct
        self.assertEqual(list.head.player, secondPlayer)
        self.assertEqual(list.head.next.player, firstPlayer)
        self.assertEqual(list.head.next.prev.player, secondPlayer)
        # test the tail reference is correct
        self.assertEqual(list.head.next, list.tail)
        # test None references for head and tail
        self.assertIsNone(list.head.prev)
        self.assertIsNone(list.tail.next)
        # test length of list correct
        self.assertEqual(list.size, 2)


    def test_push_head_to_list_of_many(self):

        list = PlayerList()

        players = [["ID123", "Bob Smith"],
                   ["ID234", "Jane Doe"],
                   ["ID456", "Mickey Mouse"],
                   ["ID567", "Donald Duck"]]
        
        players_array = []

        for player in players:
            players_array.append(Player(player[0], player[1]))
            list.push_head(players_array[-1])

        # test last two nodes added correctly and references correct
        self.assertEqual(list.head.player, players_array[-1])
        self.assertEqual(list.head.next.player, players_array[-2])
        self.assertEqual(list.head.next.prev.player, players_array[-1])
        # test tail correct
        self.assertEqual(players_array[0], list.tail.player)
        # test None references
        self.assertIsNone(list.head.prev)
        self.assertIsNone(list.tail.next)
        self.assertEqual(list.size, len(players_array))

        

# TAIL TESTS
    def test_push_tail_to_empty_list(self):
        list = PlayerList()
        firstPlayer = Player("ID123", "Bob Smith")
        list.push_tail(firstPlayer)
        # test node correctly added
        self.assertEqual(list.tail.player, firstPlayer)
        # test prev and next are correctly showing None
        self.assertIsNone(list.tail.next)
        self.assertIsNone(list.tail.prev)
        # test head and tail is the same
        self.assertEqual(list.head, list.tail)
        

    def test_push_tail_to_list_of_one(self):
        list = PlayerList()
        firstPlayer = Player("ID123", "Bob Smith")
        list.push_tail(firstPlayer)
        secondPlayer = Player("ID234", "Jane Doe")
        list.push_tail(secondPlayer)

        # test second node correctly added as the head including all 
        # references correct
        self.assertEqual(list.tail.player, secondPlayer)
        self.assertEqual(list.tail.prev.player, firstPlayer)
        self.assertEqual(list.tail.prev.next.player, secondPlayer)
        # test the head reference is correct
        self.assertEqual(list.tail.prev, list.head)
        # test None references for head and tail
        self.assertIsNone(list.head.prev)
        self.assertIsNone(list.tail.next)
        # test length of list correct
        self.assertEqual(list.size, 2)


    def test_push_tail_to_list_of_many(self):

        list = PlayerList()

        players = [["ID123", "Bob Smith"],
                   ["ID234", "Jane Doe"],
                   ["ID456", "Mickey Mouse"],
                   ["ID567", "Donald Duck"]]
        
        players_array = []

        for player in players:
            players_array.append(Player(player[0], player[1]))
            list.push_tail(players_array[-1])

        # test last two nodes added correctly and references correct
        self.assertEqual(list.tail.player, players_array[-1])
        self.assertEqual(list.tail.prev.player, players_array[-2])
        self.assertEqual(list.tail.prev.next.player, players_array[-1])
        # test tail correct
        self.assertEqual(players_array[0], list.head.player)
        # test None references
        self.assertIsNone(list.head.prev)
        self.assertIsNone(list.tail.next)
        # test size of list
        self.assertEqual(list.size, len(players_array))