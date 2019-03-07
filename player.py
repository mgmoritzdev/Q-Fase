from elo import compare


class Player:
    """ A player is an object that contains the skill level of a
person and it is composed by the elo rating of different skills.
"""

    def __init__(self, name):
        # Retrieve from persistent storage
        self.name = name
        self.defense = 1000
        self.attack = 1000
        self.creativity = 1000

    def compare_defense(self, other, score):
        """ Compare Elo rating of two players given the skill and score
in the contest."""

        reverseScore = abs(1 - score)
        s1 = self.defense
        s2 = other.defense

        self.defense = compare(s1, s2, score)
        other.defense = compare(s2, s1, reverseScore)

    def compare_attack(self, other, score):
        """ Compare Elo rating of two players given the skill and score
in the contest."""

        reverseScore = abs(1 - score)
        s1 = self.attack
        s2 = other.attack

        self.attack = compare(s1, s2, score)
        other.attack = compare(s2, s1, reverseScore)

    def compare_creativity(self, other, score):
        """ Compare Elo rating of two players given the skill and score
in the contest."""

        reverseScore = abs(1 - score)
        s1 = self.attack
        s2 = other.attack

        self.creativity = compare(s1, s2, score)
        other.creativity = compare(s2, s1, reverseScore)
