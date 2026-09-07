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


    def __str__(self):
        """Return a string representing a Player."""
        string = "Player ID: " + self._unique_id
        string += ", Player Name: " + self._player_name
        return string

    def __repr__(self):
        """Return a representation of the Player object."""
        string = self.__class__.__name__ + "(name=\'" + self.name
        string += "\', uid=\'" + self.uid + "\', score="
        string += str(self.score) + ")"
        return string

    def __lt__(self, other: Player):
        return self.score < other.score