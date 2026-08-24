class Player:
    """Represents a Player."""

    def __init__(self, unique_id: str, player_name: str):
        """Initialise the Player.

        Args:
            unique_id (str): the player's unique id
            player_name (str): the player's name
        """
        self._unique_id = unique_id
        self._player_name = player_name

    # Appropriate way to put a docstring on a property found in:
    # https://stackoverflow.com/questions/16025462/what-is-the-right-way-to-put-a-docstring-on-python-property
    @property
    def uid(self):
        """Get the Player's unique ID."""
        return self._unique_id

    @property
    def name(self):
        "Get the Player's name."
        return self._player_name

    def __str__(self):
        """Return a string representing a Player."""
        return "Player ID: " + self._unique_id + ", Player Name: " + self._player_name
