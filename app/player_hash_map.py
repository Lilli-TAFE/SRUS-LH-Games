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
            return hash(key) % self.SIZE
        else:
            return Player.hash(key) % self.SIZE

    @property
    def hashmap(self):
        return self._player_hash_array


    def __getitem__(self, key):
        player_list = self.hashmap[self.get_index(key)]
        return player_list.find_by_key(key)



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
        found_player = player_list.find_by_key(key)
        # If it isn't, create a player and add the player to the player list
        if found_player == None:
            # Add the player object or new player
            player_list.push_tail(
                key if isinstance(key, Player) else Player(key, name)
            )
        # If it is, update the player's name
        else:
            found_player.name = name

    # End of copied code ------------------------------------------------------------------

    def __len__(self):
        count = 0
        for player_list in self._player_hash_array:
            count += player_list.size

        return count

    def __delitem__(self, key):
        pass


