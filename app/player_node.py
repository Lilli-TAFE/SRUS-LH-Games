from app.player import Player


# Referenced PEP-0257 for docstring best practice
# https://peps.python.org/pep-0257/
class PlayerNode:
    """Represents a node in a PlayerList."""

    def __init__(self, player: Player, next=None, prev=None):
        """Initialise the PlayerNode.

        Args:
            player (Player): the Player object stored in the node
            next (PlayerNode): the next node in the list, None by default
            prev (PlayerNode): the previous node in the list, None by default
        """
        self._player = player
        self._next = next
        self._prev = prev

    # Appropriate way to put a docstring on a property found in:
    # https://stackoverflow.com/questions/16025462/what-is-the-right-way-to-put-a-docstring-on-python-property
    @property
    def next(self):
        """Get or set the next PlayerNode."""
        return self._next

    @next.setter
    def next(self, next: PlayerNode):
        self._next = next

    @property
    def prev(self):
        """Get or set the previous PlayerNode."""
        return self._prev

    @prev.setter
    def prev(self, prev: PlayerNode):
        self._prev = prev

    @property
    def player(self):
        """Get the Player of this node"""
        return self._player

    @property
    def key(self):
        """Get the Key of this node."""
        return self._player.uid

    def __str__(self):
        """Return a string representing a PlayerNode."""
        node_string = "Player Node: \n\tPlayer ID: " + self._player.uid
        node_string += "\n\tPlayer name: " + self._player.name
        return node_string