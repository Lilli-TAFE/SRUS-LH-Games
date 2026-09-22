from app.player import Player
from app.player_list import PlayerList
from math import pi

class PlayerHashMap:

    SIZE: int = 10

    def __init__(self):
        self._player_hash_array = []
        for _ in range(self.SIZE):
            self._player_hash_array.append(PlayerList())


    def get_index(self, key: str | Player) -> int:
        """Return the hashed array index of the key or Player"""
        if isinstance(key, Player):
            return hash(key) % self.SIZE
        else:
            return Player.lillis_made_up_hash(key) % self.SIZE


    def __getitem__(self, key):
        """Return the Player by its key"""
        player_list = self._player_hash_array[self.get_index(key)]
        return player_list.find_by_key(key).player


    def __setitem__(self, key: str, name: str) -> None:
        # TODO work out how I'm pushing a Player object as the Name!!!
        """Sets a new Player or updates the name of the existing Player"""
        # get the player's appropriate PlayerList:
        player_list = self._player_hash_array[self.get_index(key)]
        # check if the player is in the list
        node = player_list.find_by_key(key)
        found_player = None if node is None else player_list.find_by_key(key).player
        # If it isn't, create a player and add the player to the player list
        if found_player == None:
            # Add the player object or new player to tail
            player_list.push_tail(
                key if isinstance(key, Player) else Player(key, name)
            )
        # If it is, update the player's name
        else:
            found_player.name = name

    def __len__(self):
        """Return the number of Players in the map"""
        count = 0
        for player_list in self._player_hash_array:
            count += player_list.size

        return count

    def __delitem__(self, key):
        """Remove a Player from the map"""
        pass


