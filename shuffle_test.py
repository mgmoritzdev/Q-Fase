import unittest
import shuffle
from math import floor
from player_data import get_players


class ShufflerData(unittest.TestCase):
    def setUp(self):
        self.players = get_players()
        self.number_of_teams = 2
        self.shuffler = shuffle.Shuffler(self.players[0:10],
                                         self.number_of_teams)


class SimpleShufflerTestCase(unittest.TestCase):
    def setUp(self):
        self.players = get_players()
        self.number_of_teams = 2
        self.shuffler = shuffle.Shuffler(self.players,
                                         self.number_of_teams)
        self.shuffler.split_teams()


class SplitEvenNumberOfPlayersInTwoTeamsTestCase(ShufflerData):
    def runTest(self):
        self.shuffler = shuffle.Shuffler(self.players[0:10], 2)
        self.shuffler.split_teams()

        expected = expected_players_by_team(len(self.shuffler.players),
                                            self.shuffler.number_of_teams)

        team1 = self.shuffler.teams[0].players
        team2 = self.shuffler.teams[1].players
        self.assertEqual(len(team1), expected[0],
                         'Wrong number of players')
        self.assertEqual(len(team2), expected[1],
                         'Wrong number of players')


class SplitEvenNumberOfPlayersInThreeTeamsTestCase(ShufflerData):
    def runTest(self):
        self.shuffler.number_of_teams = 3
        self.shuffler.players = self.players[0:10]
        self.shuffler.split_teams()
        expected = expected_players_by_team(len(self.shuffler.players),
                                            self.shuffler.number_of_teams)
        team1 = self.shuffler.teams[0].players
        team2 = self.shuffler.teams[1].players
        team3 = self.shuffler.teams[2].players
        self.assertEqual(len(team1), expected[0],
                         'Wrong number of players')
        self.assertEqual(len(team2), expected[1],
                         'Wrong number of players')
        self.assertEqual(len(team3), expected[2],
                         'Wrong number of players')


class SplitOddNumberOfPlayersInTwoTeamsTestCase(ShufflerData):
    def runTest(self):
        self.shuffler.number_of_teams = 2
        self.shuffler.players = self.players[0:9]
        self.shuffler.split_teams()
        expected = expected_players_by_team(len(self.shuffler.players),
                                            self.shuffler.number_of_teams)
        team1 = self.shuffler.teams[0].players
        team2 = self.shuffler.teams[1].players
        self.assertEqual(len(team1), expected[0],
                         'Wrong number of players')
        self.assertEqual(len(team2), expected[1],
                         'Wrong number of players')


class CalculateDistanceBetweenTwoEqualTeams(SimpleShufflerTestCase):
    def runTest(self):
        self.assertEqual(self.shuffler.calculate_team_diff(), 0,
                         'Wrong distance')


class CalculateDistanceBetweenTwoEqualPlayers(SimpleShufflerTestCase):
    def runTest(self):
        p1 = self.shuffler.players[0]
        p2 = self.shuffler.players[1]
        distance = self.shuffler.calculate_player_diff([p1, p2])

        self.assertEqual(distance, 0, 'Wrong distance')


class CalculateDistanceBetweenTwoDifferentPlayers(SimpleShufflerTestCase):
    def runTest(self):
        make_team_strong(self.shuffler.teams[0], 1000)

        p1 = self.shuffler.players[0]
        p2 = self.shuffler.players[1]
        distance = self.shuffler.calculate_player_diff([p1, p2])

        self.assertNotEqual(distance, 0, 'Wrong distance')


class CalculateDistanceBetweenTwoDifferentTeams(SimpleShufflerTestCase):
    def runTest(self):
        team1 = self.shuffler.teams[0]
        make_team_strong(team1, 1000)
        self.assertNotEqual(self.shuffler.calculate_team_diff(), 0,
                            'Wrong distance')


class CalculateDistanceBetweenThreeEqualTeams(ShufflerData):
    def runTest(self):
        self.number_of_teams = 3
        self.shuffler = shuffle.Shuffler(self.players[0:9],
                                         self.number_of_teams)
        self.shuffler.split_teams()
        self.assertEqual(self.shuffler.calculate_team_diff(), 0,
                         'Wrong distance')


class CalculateDistanceBetweenThreeDifferentTeams(ShufflerData):
    def runTest(self):
        self.number_of_teams = 3
        self.shuffler = shuffle.Shuffler(self.players[0:9],
                                         self.number_of_teams)
        self.shuffler.split_teams()
        make_team_strong(self.shuffler.teams[0], 1000)
        self.assertNotEqual(self.shuffler.calculate_team_diff(), 0,
                            'Wrong distance')


class SwapPlayer(SimpleShufflerTestCase):
    def runTest(self):
        team0 = self.shuffler.teams[0]
        team1 = self.shuffler.teams[1]

        t0_player_index = 0
        t1_player_index = 0

        t0_player_name = team0.players[t0_player_index].name
        t1_player_name = team1.players[t1_player_index].name

        self.shuffler.swap_player(team0, team1,
                                  t0_player_index,
                                  t1_player_index)

        self.assertEqual(t0_player_name,
                         team1.players[-1].name,
                         'Swap failed')
        self.assertEqual(t1_player_name,
                         team0.players[-1].name,
                         'Swap failed')


def expected_players_by_team(number_of_players, number_of_teams):
    min_players_per_team = (floor(number_of_players / number_of_teams))
    expected_values = []

    for i in range(number_of_teams):
        rest = 1 if number_of_players % number_of_teams > i else 0
        expected_values.append(min_players_per_team + rest)

    return expected_values


def make_team_strong(team, diff):
    for player in team.players:
        for skill in player.skills:
            currentValue = getattr(player, skill)
            setattr(player, skill, currentValue + diff)


if __name__ == '__main__':
    unittest.main()
