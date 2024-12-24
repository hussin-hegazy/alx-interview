#!/usr/bin/python3

""" Contains makeChange function"""


def makeChange(coins, total):
    # If the total is zero or less, we don't need any coins
    if total <= 0:
        return 0
    # Sort the coins in decreasing order
    coins.sort(reverse=True)
    # Initialize the coin count to zero
    coin_count = 0
    # Iterate through each coin in the list of coins
    for coin in coins:
        # If the coin is greater than the remaining total, skip it
        if coin > total:
            continue
        # Calculate the number of times the current coin can be used
        count = total // coin
        # Update the total by subtracting the value of the coins used
        total -= count * coin
        # Update the coin count by adding the number of coins used
        coin_count += count
        # If the total is now zero, we're done
        if total == 0:
            break
    # If we couldn't make change for the total, return -1
    if total > 0:
        return -1
    # Otherwise, return the coin count
    return coin_count







   
