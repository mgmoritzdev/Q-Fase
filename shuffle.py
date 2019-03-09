from player import Player
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
        teams_skills = [[] for _ in range(self.number_of_teams)]
        for t in range(self.number_of_teams):
            for skill in Player.skills:
                teams_skills[t].append(self.teams[t].get_team_skill(skill))

        error = 0
        for t1 in range(0, self.number_of_teams - 1):
            for t2 in range(t1 + 1, self.number_of_teams):
                for s in range(len(Player.skills)):
                    error += calculate_error(teams_skills[t1][s],
                                             teams_skills[t2][s])
        return error

    def split_teams(self):
        number_of_players = len(self.players)
        teams = [[] for _ in range(self.number_of_teams)]
        for i in range(number_of_players):
            target_team = i % self.number_of_teams
            teams[target_team].append(self.players[i])

        self.teams = []
        for i in range(self.number_of_teams):
            self.teams.append(Team('Team' + str(i), teams[i]))


def calculate_error(v1, v2):
    return (v1 - v2) ** 2
