class Player:
    """Represents a Player."""

    def __init__(self, unique_id: str, player_name: str, player_score = 0):
        """Initialise the Player.

        Args:
            unique_id (str): the player's unique id
            player_name (str): the player's name
        """
        self._unique_id = unique_id
        self._player_name = player_name
        self.score = player_score

    # Appropriate way to put a docstring on a property found in:
    # https://stackoverflow.com/questions/16025462/what-is-the-right-way-to-put-a-docstring-on-python-property
    @property
    def uid(self):
        """Get the Player's unique ID."""
        return self._unique_id

    @property
    def name(self):
        """Get the Player's name."""
        return self._player_name

    @property
    def score(self):
        """Get the Player's score."""
        return self._score

    @score.setter
    def score(self, value):
        if (value < 0):
            raise ValueError("Score cannot be negative")
        self._score = value

    @classmethod
    def sort_players(_cls, arr):
        """Accepts an array of Players and returns a sorted array"""
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        left = []
        right = []
        for x in arr[1:]:
            if x > pivot:
                left.append(x)
            else:
                right.append(x)
        return Player.sort_players(left) + [pivot] + Player.sort_players(right)


    def __str__(self):
        """Return a string representing a Player."""
        string = "Player ID: " + self._unique_id
        string += ", Player Name: " + self._player_name
        string += ", Player score: " + str(self.score)
        return string

    def __repr__(self):
        """Return a representation of the Player object."""
        string = self.__class__.__name__ + "(name=\'" + self.name
        string += "\', uid=\'" + self.uid + "\', score="
        string += str(self.score) + ")"
        return string

    def __lt__(self, other: Player):
        return self.score < other.score

    def __eq__(self, other):
        attrs_equal = True  

        # first check if the number of attributes are the same
        if(len(self.__dict__) != len(other.__dict__)):
            attrs_equal = False

        for item in other.__dict__:
            # Check if the attrs_equal is false
            if not attrs_equal:
                break

            # Set attrs_equal to the comparison
            attrs_equal = (other.__dict__[item] == self.__dict__[item])

        return attrs_equal