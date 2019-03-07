def odds(rating_a, rating_b):
    power = (rating_b - rating_a) / 400
    # print('power: ' + str(power))
    return 1.0/(1 + 10**power)


def calculate_k(rating):
    return 16 if (rating > 2400) else (24 if (rating > 2100) else 32)


# TODO: rename to update
def compare(rating_a, rating_b, score):
    """ Return the new rating given a game between a player with rating _a
and a player with rating_b with result equals score"""
    # print test
    k = calculate_k(rating_a)
    odd = odds(rating_a, rating_b)
    # print('rating a: ' + str(rating_a))
    # print('rating b: ' + str(rating_b))
    # print('k: ' + str(k))
    # print('odds: ' + str(odd))
    return rating_a + k * (score - odd)


def game(player1, player2, score):
    reverseScore = abs(1 - score)
    player1 = compare(player1, player2, score)
    player2 = compare(player2, player1, reverseScore)
