from player import Player
from player_node import PlayerNode


class PlayerList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    @property
    def size(self):
        return self._size

    @property
    def is_empty(self):
        return self.size == 0

    
    def push_head(self, player: Player):

        if self.is_empty:
            self._head = PlayerNode(player)
            self._tail = self._head
        else:
            self._head = PlayerNode(player, self._head)
            self._head.next.prev = self._head

        self._size += 1


    def push_tail(self, player: Player):

        if self.is_empty:
            self._tail = PlayerNode(player)
            self._head = self._tail
        else:
            self._tail = PlayerNode(player, None, self._tail)
            self._tail.prev.next = self._tail

        self._size += 1


    def find_by_key(self, key):

        current_node = self.head
        keep_searching = True

        while keep_searching:
            if current_node.key == key:
                keep_searching = False
            elif current_node == self.tail:
                current_node = None
                keep_searching = False
            else:
                current_node = current_node.next

        return current_node


    def remove_head(self):
        self._head = self._head.next
        self._head.prev = None
        self._size -= 1


    def remove_tail(self):
        self._tail = self._tail.prev
        self._tail.next = None
        self._size -= 1


    def remove_by_key(self, key):

        to_remove = self.find_by_key(key)

        if to_remove == self.head:
            self.remove_head()
        elif to_remove == self.tail:
            self.remove_tail()
        else:
            to_remove.prev.next = to_remove.next
            to_remove.next.prev = to_remove.prev

        self._size -= 1

    def display(self, forward = True):
        current = self.head
        display_string = "\n\n--- Player List ---\n\n"

        while current != None:
            display_string += str(current) + "\n"
            current = current.next if forward else current.prev

        display_string += "\n----- END -----\n\n"
        return display_string
