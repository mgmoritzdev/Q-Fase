# from player import Player
from team import Team
from math import floor


class Shuffler:

    def __init__(self, players, number_of_teams):
        self.players = players
        self.number_of_teams = number_of_teams

    def shuffle(self):
        """Receive players and returns balaced teams. The shuffle algorithm will try
to balance all the all the skills in both teams."""
        self.teamA = Team(self.players)
        self.teamB = Team(self.players)
        pass

    def swap_random_player(self):
        pass

    def calculate_diff(self):
        pass

    def split_teams(self):
        number_of_players = len(self.players)
        player_per_team = floor(len(self.players) / self.number_of_teams)
        teams = [[] for _ in range(self.number_of_teams)]
        for i in range(number_of_players):
            target_team = i % self.number_of_teams
            teams[target_team].append(self.players[i])

        self.teams = []
        for i in range(self.number_of_teams):
            self.teams.append(Team('Team' + str(i), teams[i]))

# return {'teamA': {}, 'teamB':{}}
