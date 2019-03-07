from elo import compare
from math import floor
from functools import reduce


class Player:
    """ A player is an object that contains the skill level of a
person and it is composed by the elo rating of different skills.
"""

    player_attributes = ['defense', 'attack',
                         'creativity', 'team_play']

    def __init__(self, name):
        # Retrieve from persistent storage
        self.name = name
        self.init_attributes()

    def compare_attr(self, other, attr, score):
        """ Compare Elo rating of two players given the skill and score
in the contest."""

        reverseScore = abs(1 - score)
        s1 = getattr(self, attr)
        s2 = getattr(other, attr)
        setattr(self, attr, compare(s1, s2, score))
        setattr(other, attr, compare(s2, s1, reverseScore))

    def init_attributes(self):
        for attr in self.player_attributes:
            setattr(self, attr, 1000)

    def get_average_score(self):
        scores = map(lambda x: getattr(self, x), self.player_attributes)
        return reduce(lambda x, y: x + y, scores) / len(self.player_attributes)

    def print_score(self):
        text = '{:10}'.format(self.name) + ' |'
        for attr in self.player_attributes:
            text += ' ' + attr + ': '
            text += '{:>4}'.format(str(floor(getattr(self, attr))))
            text += ';'
        text += ' avg: '
        text += '{:>4}'.format(str(floor(self.get_average_score())))
        text += ';'
        print(text)
