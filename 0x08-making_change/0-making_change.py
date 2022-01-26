#!/usr/bin/python3

def makeChange(coins, total):
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
