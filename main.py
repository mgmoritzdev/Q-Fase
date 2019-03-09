from player import Player
from team import Team
from random import random
from math import floor


p1 = Player('Marcos')
p2 = Player('Maradona')
p3 = Player('Raoni')
p4 = Player('Renato')
p5 = Player('Álvaro')
p6 = Player('Caio')
p7 = Player('Daniel')
p8 = Player('Michael')
p9 = Player('Diogo')
p10 = Player('Marcelo')
p11 = Player('Junior')
p12 = Player('Silvio')
p13 = Player('Fernandes')
p14 = Player('Reinaldo')
p15 = Player('Adauto')
p16 = Player('Sandro')

all_players = [p1, p2, p3, p4, p5, p6, p7, p8,
               p9, p10, p11, p12, p13, p14, p15, p16]

t1 = Team('Team A', [p1, p2, p3, p4, p5, p6, p7, p8])
t2 = Team('Team B', [p9, p10, p11, p12, p13, p14, p15, p16])


def get_random_player():
    index = floor(random() * len(all_players))
    return all_players[index]


def get_random_skills():
    index = floor(random() * len(Player.skills))
    return Player.skills[index]


def generate_random_game():
    player1 = get_random_player()
    player2 = get_random_player()

    random_score = random()

    if (player1 != player2):
        player1.update_skill_level(player2, get_random_skills(), random_score)


def make_team_strong(team):
    for player in team.players:
        for skill in player.skills:
            currentValue = getattr(player, skill)
            setattr(player, skill, currentValue + 1000)


def generate_random_state():
    make_team_strong(t1)
    for i in range(1, 1000):
        generate_random_game()


generate_random_state()

t1.print_all_skills()
t2.print_all_skills()
