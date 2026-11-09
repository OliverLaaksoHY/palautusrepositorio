"""Module fo calculating things related to playerstats"""

from reader import PlayerReader
from player import Player
def scorer(p: Player):
    """Function that returns player score"""
    return p.goals + p.assists
class PlayerStats():
    """Class that deals with playerstats"""
    def __init__(self, pr: PlayerReader):
        """init"""
        self.players = pr.get_players()

    def top_scorers_by_nationality(self, country: str):
        """top scorers"""
        players = []

        for player in self.players:
            if player.nationality == country:
                players.append(player)
        players.sort(key=scorer, reverse=True)
        return players
    def str(self):
        """strreturn"""
        return self.players
