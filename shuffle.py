# from player import Player
from team import Team


class Shuffler:

    def __init__(self, players):
        self.players = players
        self.split_teams()

    def shuffle(self):
        """Receive players and returns balaced teams. The shuffle algorithm will try
to balance all the all the skills in both teams."""
        self.teamA = Team(self.players)
        self.teamB = Team(self.players)
        pass

    def calculate_diff(self):
        pass

    def split_teams(self):
        pass

# return {'teamA': {}, 'teamB':{}}
