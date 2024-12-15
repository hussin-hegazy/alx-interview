#!/usr/bin/python3
"""Module defining the isWinner function and related helper functions."""


def isWinner(x, nums):
    """Function to get who has won in prime game"""
    mariaWinsCount = 0
    benWinsCount = 0

    for num in nums:
        roundsSet = list(range(1, num + 1))
        primesSet = primes_in_range(1, num)

        if not primesSet:
            benWinsCount += 1
            continue

        isMariaTurns = True

        while(True):
            if not primesSet:
                if isMariaTurns:
                    benWinsCount += 1
                else:
                    mariaWinsCount += 1
                break

            smallestPrime = primesSet.pop(0)
            roundsSet.remove(smallestPrime)

            roundsSet = [x for x in roundsSet if x % smallestPrime != 0]

            isMariaTurns = not isMariaTurns
ش#!/usr/bin/python3
"""Module defining the isWinner function and related helper functions."""

def sieve_of_eratosthenes(limit):
    """Generate a list of prime numbers up to the given limit using the Sieve of Eratosthenes algorithm.
    
    Args:
        limit (int): The maximum number to check for primality.
    
    Returns:
        list: A list of prime numbers up to the given limit.
    """
    is_prime = [True] * (limit + 1)  # Create a list to track prime status for numbers up to the limit
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
    
    for i in range(2, int(limit ** 0.5) + 1):  # Iterate up to the square root of the limit
        if is_prime[i]:  # If the number is still marked as prime
            for j in range(i * i, limit + 1, i):  # Mark all multiples of i as non-prime
                is_prime[j] = False
    
    primes = [i for i in range(limit + 1) if is_prime[i]]  # Extract all numbers that are still marked as prime
    return primes

def play_round(n, primes):
    """Simulate a single round of the prime game for a given n.
    
    Args:
        n (int): The upper limit of numbers for this round.
        primes (list): A list of prime numbers up to the maximum number in the rounds.
    
    Returns:
        str: The winner of the round ("Maria" or "Ben").
    """
    player_turn = "Maria"  # Maria starts first
    numbers = list(range(1, n + 1))  # List of numbers from 1 to n


    if mariaWinsCount > benWinsCount:
        return "Winner: Maria"

    if mariaWinsCount < benWinsCount:
        return "Winner: Ben"

    return None


def is_prime(n):
    """Returns True if n is prime, else False."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primes_in_range(start, end):
    """Returns a list of prime numbers between start and end (inclusive)."""
    primes = [n for n in range(start, end+1) if is_prime(n)]
    return primes
