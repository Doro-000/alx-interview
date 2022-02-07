#!/usr/bin/python3
"""
Maria and Ben are playing a game.
Given a set of consecutive integers starting from 1 up to and including n,
they take turns choosing a prime number from the set and removing that number
and its multiples from the set.
The player that cannot make a move loses the game.

They play x rounds of the game, where n may be different for each round.
Assuming Maria always goes first and both players play optimally,
determine who the winner of each game is.
"""


def isWinner(x, nums):
    """
    implementaion
    """
    scores = [['maria', 0], ['ben', 0]]
    turn = 0
    for i in range(x):
        bucket = [num for num in range(1, nums[i] + 1)]
        while (len(bucket) != 1):
            bucket = list(filter(lambda x: x % bucket[1] != 0, bucket))
            turn ^= 1
        scores[turn ^ 1][1] += 1
        turn = 0
    scores = dict(scores)
    if scores['maria'] == scores['ben']:
        return None
    return sorted(scores, key=lambda key: scores[key])[1]
