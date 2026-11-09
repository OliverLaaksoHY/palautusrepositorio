"""Module that implements Playre class"""
class Player:
    """placeholder"""
    def __init__(self, player_dict):
        """placeholder"""
        self.name = player_dict["name"]
        self.nationality = player_dict["nationality"]
        self.assists = player_dict["assists"]
        self.goals = player_dict["goals"]
        self.team = player_dict["team"]
        self.games = player_dict["games"]

    def __str__(self):
        """placeholder"""
        one = f"{self.name:20} {self.team:20} {self.goals:2}"
        two = f"{self.assists:2} = {self.goals + self.assists}"
        return one+two
    def __repr__(self):
        """placeholder"""
        return self.name
