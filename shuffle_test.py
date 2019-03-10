import unittest
import shuffle
from math import floor
from team import Team
from player import Player
from player_data import get_players
from random import random


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

        shuffle.swap_player(team0, team1,
                            t0_player_index,
                            t1_player_index)

        self.assertEqual(t0_player_name,
                         team1.players[-1].name,
                         'Swap failed')
        self.assertEqual(t1_player_name,
                         team0.players[-1].name,
                         'Swap failed')


class GetSwapCandidate(SimpleShufflerTestCase):
    def runTest(self):
        team1, team2, p_idx_1, p_idx_2 = self.shuffler.get_swap_candidate()

        self.assertIsInstance(team1, Team, 'Getting swap candidate failed')
        self.assertIsInstance(team1.players[p_idx_1], Player,
                              'Getting swap candidate failed')
        self.assertIsInstance(team2, Team, 'Getting swap candidate failed')
        self.assertIsInstance(team2.players[p_idx_2], Player,
                              'Getting swap candidate failed')


class CalculateSwapEffect(SimpleShufflerTestCase):
    def runTest(self):
        team1, team2, p_idx_1, p_idx_2 = self.shuffler.get_swap_candidate()
        make_team_strong(team1, 100)

        swap_effect = (self.shuffler
                       .calculate_swap_effect(team1, team2, p_idx_1, p_idx_2))
        # team1.players[p_idx_1].print_score()
        # team2.players[p_idx_2].print_score()
        self.assertIsInstance(swap_effect, float,
                              'Swap effect wrong result type')
        self.assertTrue(swap_effect < 0, 'Swap effect should be negative')


class Shuffle(SimpleShufflerTestCase):
    def runTest(self):
        team_0 = self.shuffler.teams[0]
        team_1 = self.shuffler.teams[1]

        make_team_strong(team_0, 500)
        generate_random_state(self.players, 1000)

        # team_0.print_all_skills()
        # team_1.print_all_skills()

        print('diff before: ' + str(self.shuffler.calculate_team_diff()))
        self.shuffler.shuffle(100)

        team_0.print_all_skills()
        team_1.print_all_skills()

        # for team in self.shuffler.teams:
        #     print(team.name)
        #     for player in team.players:
        #         player.print_score()

        print('diff after: ' + str(self.shuffler.calculate_team_diff()))


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


def generate_random_state(players, iterations):
    for i in range(1, iterations):
        generate_random_game(players)


def get_random_player(players):
    index = floor(random() * len(players))
    return players[index]


def get_random_skill():
    index = floor(random() * len(Player.skills))
    return Player.skills[index]


def generate_random_game(players):
    player1 = get_random_player(players)
    player2 = get_random_player(players)

    random_score = random()

    if (player1 != player2):
        player1.update_skill_level(player2, get_random_skill(), random_score)


if __name__ == '__main__':
    unittest.main()
