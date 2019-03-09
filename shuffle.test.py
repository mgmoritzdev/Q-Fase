import unittest
import shuffle
from player import Player
from math import floor


class ShufflerData(unittest.TestCase):
    def setUp(self):
        self.players = get_players()
        self.number_of_teams = 2
        self.shuffler = shuffle.Shuffler(self.players[0:10],
                                         self.number_of_teams)
        self.shuffler.split_teams()


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


def get_players():
    p1 = Player('Marcos')
    p2 = Player('Maradona')
    p3 = Player('Raoni')
    p4 = Player('Renato')
    p5 = Player('Álvaro')
    p6 = Player('Caio')
    p7 = Player('Daniel')
    p8 = Player('Michael')
    p9 = Player('Diogo')
    p10 = Player('Marcelo')
    p11 = Player('Junior')
    p12 = Player('Silvio')
    p13 = Player('Fernandes')
    p14 = Player('Reinaldo')
    p15 = Player('Adauto')
    p16 = Player('Sandro')

    return [p1, p2, p3, p4, p5, p6, p7, p8, p9,
            p10, p11, p12, p13, p14, p15, p16]


def expected_players_by_team(number_of_players, number_of_teams):
    min_players_per_team = (floor(number_of_players / number_of_teams))
    expected_values = []

    for i in range(number_of_teams):
        rest = 1 if number_of_players % number_of_teams > i else 0
        expected_values.append(min_players_per_team + rest)

    return expected_values



if __name__ == '__main__':
    unittest.main()


# class FrameSpareBeforeExtraBallTestCase(SimpleFrameTestCase):
#     def runTest(self):
#         self.frame.throw(6)
#         self.frame.throw(4)
#         self.assertEqual(self.frame.points, 10, 'Wrong score')
#         self.assertEqual(self.frame.extraBalls, 1, 'Wrong extra balls')


# class FrameSpareAfterExtraBallTestCase(SimpleFrameTestCase):
#     def runTest(self):
#         self.frame.throw(6)
#         self.frame.throw(4)
#         self.frame.throw(3)  # accepted in favor of last frame
#         self.frame.throw(7)  # ignored
#         self.assertEqual(self.frame.points, 13, 'Wrong score')
#         self.assertEqual(self.frame.extraBalls, 0, 'Wrong extra balls')


# class FrameStrikeBeforeExtraBallsTestCase(SimpleFrameTestCase):
#     def runTest(self):
#         self.frame.throw(10)
#         self.assertEqual(self.frame.points, 10, 'Wrong score')
#         self.assertEqual(self.frame.extraBalls, 2, 'Wrong extra balls')


# class FrameStrikeAfterFirstExtraBallTestCase(SimpleFrameTestCase):
#     def runTest(self):
#         self.frame.throw(10)
#         self.frame.throw(10)
#         self.assertEqual(self.frame.points, 20, 'Wrong score')
#         self.assertEqual(self.frame.extraBalls, 1, 'Wrong extra balls')


# class FrameStrikeAfterSecondExtraBallTestCase(SimpleFrameTestCase):
#     def runTest(self):
#         self.frame.throw(10)
#         self.frame.throw(7)
#         self.frame.throw(3)  # accepted in favor of last frame
#         self.frame.throw(6)  # ignored
#         self.assertEqual(self.frame.points, 20, 'Wrong score')
#         self.assertEqual(self.frame.extraBalls, 0, 'Wrong extra balls')
