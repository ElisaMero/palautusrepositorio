import unittest
from statistics_service import StatisticsService
from player import Player
from enum_sort import SortBy


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_player_name(self):
        self.assertEqual(
            str(self.stats.search("Semenko")), "Semenko EDM 4 + 12 = 16")

    def test_player_name_wrong(self):
        name = "Nope"
        self.assertEqual(self.stats.search(
            name), None)

    def test_team_name(self):
        team_name = "PIT"
        name_list = self.stats.team(team_name)
        self.assertEqual(str(name_list[0]), "Lemieux PIT 45 + 54 = 99")
        self.assertEqual(len(name_list), 1)

    def test_top_function(self):
        how_many = 2
        top_list = self.stats.top(how_many, SortBy.POINTS)
        self.assertEqual(str(top_list[0]), "Gretzky EDM 35 + 89 = 124")
        self.assertEqual(len(self.stats.top(2, SortBy.POINTS)), how_many)

    def test_top_goal_people(self):
        top_list = self.stats.top(2, SortBy.GOALS)
        self.assertEqual(str(top_list[0]), "Lemieux PIT 45 + 54 = 99")

    def test_top_assist_people(self):
        top_list = self.stats.top(2, SortBy.ASSISTS)
        self.assertEqual(str(top_list[0]), "Gretzky EDM 35 + 89 = 124")

    def test_top_function_one_parameter(self):
        top_list = self.stats.top(2)
        self.assertEqual(str(top_list[0]), "Gretzky EDM 35 + 89 = 124")
