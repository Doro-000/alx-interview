#!/usr/bin/python3
"""
Coin change problem
Given a pile of coins of different values, determine the
fewest number of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    implementation
    """
    if total <= 0:
        return 0
    ans = 0
    for coin in sorted(coins)[::-1]:
        while (total >= coin):
            total -= coin
            ans += 1
        if not total:
            return ans
    if total:
        return -1
