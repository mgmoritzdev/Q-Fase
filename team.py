from functools import reduce
from player import Player


class Team:
    """A team is a set of players and is grouped to allow evaluation of player
skills insid the group"""
    def __init__(self, name, players):
        self.name = name
        self.players = players

    def get_team_skill(self, skill):
        """Return the average value of a given skill of the team as a whole."""
        scores = map(lambda x: getattr(x, skill), self.players)
        return reduce(lambda x, y: x + y, scores) / len(self.players)

    def print_all_skills(self):
        print(self.name + ' skills:')
        for skill in Player.skills:
            self.print_skill(skill)

    def print_skill(self, skill):
        print(skill + ': ' + str(self.get_team_skill(skill)))

    def get_team_average_strenght(self):
        """Return the average value of all skills of a team."""
        scores = []
        for skill in Player.skills:
            scores.append(self.get_team_skill(skill))
        return reduce(lambda x, y: x + y, scores) / len(Player.skills)
