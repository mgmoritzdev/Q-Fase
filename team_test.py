import unittest
from team import Team
from player import Player
from player_data import get_players
# from math import floor


class TeamData(unittest.TestCase):
    def setUp(self):
        self.players = get_players()


class SimpleTeamTestCase(unittest.TestCase):
    def setUp(self):
        self.players = get_players()[0:10]
        self.team = Team('Team1', self.players)
        self.assertEqual(self.team.players, self.players,
                         'The players were not correctly assigned to the team')


class GetAveragePlayersSkillValueTestCase(SimpleTeamTestCase):
    def runTest(self):
        self.assertEqual(self.team.get_team_skill('attack'), 1000,
                         'Wrong attack value')
        self.team.players[0].attack = 0
        num_players = len(self.team.players)
        expected = 1000 * (1 - 1/num_players)
        self.assertEqual(self.team.get_team_skill('attack'), expected,
                         'Wrong attack value')


class GetAverageTeamSkillValueTestCase(SimpleTeamTestCase):
    def runTest(self):
        self.assertEqual(self.team.get_team_skill('attack'), 1000,
                         'Wrong attack value')
        self.team.players[0].attack = 0
        num_players = len(self.team.players)
        num_skills = len(Player.skills)
        expected = 1000 * (1 - 1/(num_players * num_skills))
        self.assertEqual(self.team.get_team_average_strenght(), expected,
                         'Wrong attack value')


if __name__ == '__main__':
    unittest.main()
