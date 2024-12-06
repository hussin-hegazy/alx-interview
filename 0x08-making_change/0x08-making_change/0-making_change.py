#!/usr/bin/python3

""" Contains makeChange function"""
def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet the total amount.

    Args:
        coins (list): List of coin denominations.
        total (int): Total amount to make change for.

    Returns:
        int: Fewest number of coins needed, or -1 if not possible.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)  # ترتيب العملات من الأكبر إلى الأصغر
    count = 0
    for coin in coins:
        if total <= 0:
            break
        count += total // coin
        total %= coin

    return count if total == 0 else -1
