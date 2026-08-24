from app.player import Player
from app.player_node import PlayerNode


class PlayerList:
    """A class to store players in a linked list."""

    def __init__(self):
        """Initialise the PlayerList. No args required."""
        self._head = None
        self._tail = None
        self._size = 0

    @property
    def head(self):
        """Return the head PlayerNode of the PlayerList."""
        return self._head

    @property
    def tail(self):
        """Return the tail PlayerNode of the PlayerList."""
        return self._tail

    @property
    def size(self):
        """Return the number of Players in the PlayerList."""
        return self._size

    @property
    def is_empty(self):
        """Return True if the PlayerList is empty."""
        return self.size == 0

    def push_head(self, player: Player):
        """Insert a Player at the head of the PlayerList."""
        if self.is_empty:
            self._head = PlayerNode(player)
            self._tail = self._head
        else:
            self._head = PlayerNode(player, self._head)
            self._head.next.prev = self._head

        self._size += 1

    def push_tail(self, player: Player):
        """Insert a Player at the tail of the PlayerList."""
        if self.is_empty:
            self._tail = PlayerNode(player)
            self._head = self._tail
        else:
            self._tail = PlayerNode(player, None, self._tail)
            self._tail.prev.next = self._tail

        self._size += 1

    def find_by_key(self, key):
        """Return the first node that matches the key provided."""
        current_node = self.head
        searching = True

        while searching:
            if current_node.key == key:
                searching = False
            elif current_node == self.tail:
                current_node = None
                searching = False
            else:
                current_node = current_node.next

        return current_node

    def remove_head(self):
        """Remove the head node from the PlayerList."""
        self._head = self._head.next
        self._head.prev = None
        self._size -= 1

    def remove_tail(self):
        """Remove the tail node from the PlayerList."""
        self._tail = self._tail.prev
        self._tail.next = None
        self._size -= 1

    def remove_by_key(self, key):
        """Remove the first node that matches the key from the PlayerList."""
        to_remove = self.find_by_key(key)

        if to_remove == self.head:
            self.remove_head()
        elif to_remove == self.tail:
            self.remove_tail()
        else:
            to_remove.prev.next = to_remove.next
            to_remove.next.prev = to_remove.prev

        self._size -= 1

    def display(self, forward=True):
        """Return a string representing the PlayerList."""
        current = self.head
        display_string = "\n\n--- Player List ---\n\n"

        while current != None:
            display_string += str(current) + "\n"
            current = current.next if forward else current.prev

        display_string += "\n----- END -----\n\n"
        return display_string
