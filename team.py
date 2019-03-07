class Team:
    """A team is a set of players and is grouped to allow evaluation of player
skills insid the group"""
    def __init__(self, name, players):
        self.name = name
        self.players = players

    def assess_defense(self):
        """Return the average defensive skills of the team as a whole."""
        pass

    def assess_attack(self):
        """Return the average attacking skills of the team as a whole."""
        pass

    def assess_creativity(self):
        """Return the average creativity skills of the team as a whole."""
        pass
