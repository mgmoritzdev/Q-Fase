from player import Player
from team import Team
from random import random
from math import floor
from copy import deepcopy


class Shuffler:

    def __init__(self, players, number_of_teams):
        self.players = players
        self.number_of_teams = number_of_teams

    def shuffle(self, iterations=10):
        """Receive players and returns balaced teams. The shuffle algorithm will try
to balance all the all the skills in both teams."""

        for i in range(1, iterations):
            s0_t1, s0_t2, s0_p1_index, s0_p2_index = self.get_swap_candidate()
            s1_t1, s1_t2, s1_p1_index, s1_p2_index = self.get_swap_candidate()
            s2_t1, s2_t2, s2_p1_index, s2_p2_index = self.get_swap_candidate()

            swap_effect_0 = self.calculate_swap_effect(s0_t1, s0_t2,
                                                       s0_p1_index,
                                                       s0_p2_index)
            swap_effect_1 = self.calculate_swap_effect(s1_t1, s1_t2,
                                                       s1_p1_index,
                                                       s1_p2_index)
            swap_effect_2 = self.calculate_swap_effect(s2_t1, s2_t2,
                                                       s2_p1_index,
                                                       s2_p2_index)

            swap_array = [swap_effect_0, swap_effect_1, swap_effect_2]
            swap_index = swap_array.index(min(swap_array))

            if (min(swap_array) > 0 and random() > 0.6):
                continue

            if swap_index == 0:
                swap_player(s0_t1, s0_t2, s0_p1_index, s0_p2_index)
            elif swap_index == 1:
                swap_player(s1_t1, s1_t2, s1_p1_index, s1_p2_index)
            else:
                swap_player(s2_t1, s2_t2, s2_p1_index, s2_p2_index)

    def get_swap_candidate(self):
        """() => [Team, Team, int, int]. Get candidate arguments to be used in
swap_player."""
        team1, team2 = self.get_random_team_pair()
        p1_index = floor(random() * len(team1.players))
        p2_index = floor(random() * len(team2.players))

        return [team1, team2, p1_index, p2_index]

    def calculate_swap_effect(self, team1, team2,
                              player_index_t1, player_index_t2):
        """(Team, Team, int, int) => float. Calculates the effect of
swapping players. Negative is good."""
        diff_before = self.calculate_team_diff()
        t1 = deepcopy(team1)
        t2 = deepcopy(team2)
        swap_player(t1, t2, player_index_t1, player_index_t2)
        diff_after = calculate_team_diff([t1, t2])
        return diff_after - diff_before

    def get_team_skillsets(self):
        return get_team_skillsets(self.teams)

    def get_player_skillsets(self, players):
        number_of_players = len(players)
        players_skills = [[] for _ in range(number_of_players)]
        for p in range(number_of_players):
            for skill in Player.skills:
                players_skills[p].append(getattr(players[p], skill))
        return players_skills

    def calculate_team_diff(self):
        teams_skillsets = self.get_team_skillsets()
        return calculate_error_by_skillsets(teams_skillsets)

    def calculate_player_diff(self, players):
        players_skills = self.get_player_skillsets(players)
        return calculate_error_by_skillsets(players_skills)

    def split_teams(self):
        number_of_players = len(self.players)
        teams = [[] for _ in range(self.number_of_teams)]
        for i in range(number_of_players):
            target_team = i % self.number_of_teams
            teams[target_team].append(self.players[i])

        self.teams = []
        for i in range(self.number_of_teams):
            self.teams.append(Team('Team' + str(i), teams[i]))

    def get_random_team_pair(self):
        team_idx_pair = get_random_index_pair(len(self.teams))
        team_pair = map(lambda x: self.teams[x], team_idx_pair)
        return list(team_pair)


def calculate_error(v1, v2):
    return (v1 - v2) ** 2


def calculate_error_by_skillsets(skillsets):
    number_of_skillsets = len(skillsets)
    error = 0
    for t1 in range(0, number_of_skillsets - 1):
        for t2 in range(t1 + 1, number_of_skillsets):
            for s in range(len(Player.skills)):
                error += calculate_error(skillsets[t1][s],
                                         skillsets[t2][s])
    return error


def get_random_index_pair(array_length):
    index_pair = []
    while (len(index_pair) < 2):
        index = floor(random() * array_length)
        if (len(index_pair) == 0 or (len(index_pair) == 1
                                     and index_pair[0] != index)):
            index_pair.append(index)

    return index_pair


def get_team_skillsets(teams):
    num_teams = len(teams)
    teams_skills = [[] for _ in range(num_teams)]
    for t in range(num_teams):
        for skill in Player.skills:
            teams_skills[t].append(teams[t].get_team_skill(skill))
    return teams_skills


def swap_player(team1, team2, player_index_t1, player_index_t2):
    """(Team, Team, int, int) => void. Swaps player with player_index_t1 in team1
with player with player_index_t2 in team2."""
    player_from_t1 = team1.players.pop(player_index_t1)
    player_from_t2 = team2.players.pop(player_index_t2)

    team1.players.append(player_from_t2)
    team2.players.append(player_from_t1)


def calculate_team_diff(teams):
    teams_skillsets = get_team_skillsets(teams)
    return calculate_error_by_skillsets(teams_skillsets)
