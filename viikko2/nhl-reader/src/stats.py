from reader import PlayerReader
from player import Player
def SortByScore(p: Player):
    return p.goals + p.assists

class PlayerStats():
    def __init__(self, pr: PlayerReader):
        self.players = pr.get_players()

    def top_scorers_by_nationality(self, country: str):
        players = []

        for player in self.players:
            if player.nationality == country:
                players.append(player)
        players.sort(key=SortByScore, reverse=True)
        return players

