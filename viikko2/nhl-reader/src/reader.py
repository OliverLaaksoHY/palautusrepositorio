"""Module for reading playerdata"""
import requests
from player import Player
class PlayerReader():
    """placeholder"""
    def __init__(self, url: str):
        """placeholder"""
        self.response = requests.get(url, timeout=10).json()
    def get_players(self):
        """placeholder"""
        players = []
        for player_dict in self.response:
            player = Player(player_dict)
            players.append(player)
        return players
    def __str__(self):
        """placeholder"""
        return self.response
