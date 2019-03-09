import unittest
from team.team import Team
from player.data import get_players
# from math import floor


class TeamData(unittest.TestCase):
    def setUp(self):
        self.players = get_players()


class SimpleTeamTestCase(unittest.TestCase):
    def setUp(self):
        self.team = Team(self.players)


class SplitEvenNumberOfPlayersInTwoTeamsTestCase(SimpleTeamTestCase):
    def runTest(self):
        self.assertEqual(True, True, 'Wrong!')


if __name__ == '__main__':
    unittest.main()
