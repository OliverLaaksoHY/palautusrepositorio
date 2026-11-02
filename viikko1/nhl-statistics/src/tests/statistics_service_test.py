import unittest
from statistics_service import StatisticsService
from statistics_service import SortBy
from player import Player
class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_name_search_find(self):
        name = self.stats.search("Semenko").name
        self.assertEqual(name, "Semenko")
    
    def test_name_search_not_found(self):
        name = self.stats.search("Lorem Ipsum")
        self.assertEqual(name, None)
    
    def test_team_found(self):
        players = self.stats.team("EDM")
        namelist = [player.name for player in players]
        self.assertEqual(namelist, ["Semenko", "Kurri", "Gretzky"])

    def test_top_correct(self):
        topPlayer = self.stats.top(1)[0].name
        self.assertEqual(topPlayer, "Gretzky")
    
    def test_top_correct_goal(self):
        topPlayer = self.stats.top(1, SortBy.GOALS)[0].name
        self.assertEqual(topPlayer, "Lemieux")
    
    def test_top_correct_assist(self):
        topPlayer = self.stats.top(1, SortBy.ASSISTS)[0].name
        self.assertEqual(topPlayer, "Gretzky")
    
    
