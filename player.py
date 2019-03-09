from elo import calculate_new_rating
from math import floor
from functools import reduce


class Player:
    """ A player is an object that contains the skill level of a
person and it is composed by the elo rating of different skills.
"""

    skills = ['defense', 'attack',
              'creativity', 'team_play']

    def __init__(self, name):
        # Retrieve from persistent storage
        self.name = name
        self.init_skills()

    def update_skill_level(self, other, skill, score):
        """ Compare Elo rating of two players given the skill and score
in the contest."""

        reverseScore = abs(1 - score)
        s1 = getattr(self, skill)
        s2 = getattr(other, skill)
        setattr(self, skill, calculate_new_rating(s1, s2, score))
        setattr(other, skill, calculate_new_rating(s2, s1, reverseScore))

    def init_skills(self):
        for skill in self.skills:
            setattr(self, skill, 1000)

    def get_average_score(self):
        scores = map(lambda x: getattr(self, x), self.skills)
        return reduce(lambda x, y: x + y, scores) / len(self.skills)

    def print_score(self):
        text = '{:10}'.format(self.name) + ' |'
        for skill in self.skills:
            text += ' ' + skill + ': '
            text += '{:>4}'.format(str(floor(getattr(self, skill))))
            text += ';'
        text += ' avg: '
        text += '{:>4}'.format(str(floor(self.get_average_score())))
        text += ';'
        print(text)
