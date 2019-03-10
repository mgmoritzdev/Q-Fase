from player import Player
from team import Team


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

    def swap_player(self, team1, team2, player_index_t1, player_index_t2):
        player_from_t1 = team1.players.pop(player_index_t1)
        player_from_t2 = team2.players.pop(player_index_t2)

        team1.players.append(player_from_t2)
        team2.players.append(player_from_t1)

    def get_team_skillsets(self):
        teams_skills = [[] for _ in range(self.number_of_teams)]
        for t in range(self.number_of_teams):
            for skill in Player.skills:
                teams_skills[t].append(self.teams[t].get_team_skill(skill))
        return teams_skills

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
