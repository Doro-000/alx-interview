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
    scores = [['Maria', 0], ['Ben', 0]]
    turn = 0
    for i in range(x):
        bucket = [num for num in range(2, nums[0] + 1)]
        while (bucket):
            bucket = list(filter(lambda x: x % bucket[0] != 0, bucket))
            turn ^= 1
        scores[turn ^ 1][1] += 1
        turn = 0
        nums.append(nums.pop(0))
    scores = dict(scores)
    if scores['Maria'] == scores['Ben']:
        return None
    return sorted(scores, key=lambda key: scores[key], reverse=True)[0]
