#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to make a change
    """
    if total <= 0:
        return 0

    temporary_value = 0
    coins.sort(reverse=True)

    for coin in coins:
        if total >= coin:
            temporary_value += total // coin
            total = total % coin

    return temporary_value if total == 0 else -1
