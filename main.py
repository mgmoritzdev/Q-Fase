# from elo import compare
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

t1 = Team('t', [p1, p2, p3, p4, p5, p6, p7, p8])
t2 = Team('t', [p9, p10, p11, p12, p13, p14, p15, p16])


def get_random_player():
    index = floor(random() * len(all_players))
    return all_players[index]


def get_random_attribute():
    index = floor(random() * len(Player.player_attributes))
    return Player.player_attributes[index]


def generate_random_game():
    player1 = get_random_player()
    player2 = get_random_player()

    random_score = random()
    # if (player1.name == 'Marcos'):
    #     random_score = 1

    # if (player2.name == 'Marcos'):
    #     random_score = 0

    if (player1 != player2):
        player1.compare_attr(player2, get_random_attribute(), random_score)


def generate_random_state():
    for i in range(1, 1000):
        generate_random_game()


generate_random_state()


for player in all_players:
    player.print_score()
