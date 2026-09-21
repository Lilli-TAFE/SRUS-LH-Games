from player import Player
from player_list import PlayerList
from math import pi

class PlayerHashMap:

    SIZE: int = 10

    def __init__(self):
        self._player_hash_array = []
        for _ in range(self.SIZE):
            self._player_hash_array.append(PlayerList())

    # The following code copied from assessment documentation -----------------------------
    def get_index(self, key: str | Player) -> int:
        if isinstance(key, Player):
            return hash(key) % self.SIZE # TODO: implement __hash__ in player
        else:
            return Player.hash(key) % self.SIZE # TODO implement a hash class method in Player

    def __getitem__(self, key):
        pass

    def __setitem__(self, key: str, name: str) -> None:
        """ Psuedo code:
        1. Use the key to calculate an index into the hash map *** 
        (TODO: Implement a hash function in the Player class that returns a player hash and then modulate it by the size of the hashmap)
        2. Get the PlayerList at that index
        3. Check if the player is already on that player list.
            If it is, update the player's name.
            If it isn't, create a player and add the player to the player list.

        """
        # get the player's appropriate PlayerList:
        player_list = self.hashmap[self.get_index(key)]
        # check if the player is in the list
        # If it is, update the player's name
        # If it isn't, create a player and add the player to the player list

    # End of copied code ------------------------------------------------------------------

    def __len__(self):
        pass

    def __delitem__(self, key):
        pass

    def lillis_made_up_hash(self, key: str) -> int:

        # Using a prime number promotes even distribution of the keys 
        # in the array. This is a Mersenne prime with 39 digits in 
        # base 10: https://www.mersenne.org/primes/
        multiply_constant = (2**127)-1
        key_numeric_value = 0
        # Calculate a numeric value of the key based on ascii value of
        # each character
        for i in key:
            # Reference: How to get the ascii value of a character:
            # https://stackoverflow.com/questions/227459/how-to-get-the-ascii-value-of-a-character
            key_numeric_value += ord(i)

        hash = key_numeric_value * multiply_constant

        return hash


    def __hash__(self):
        pass
