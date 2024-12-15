#!/usr/bin/python3
"""Module defining the isWinner function and related helper functions."""

def sieve_of_eratosthenes(limit):
    """Generate a list of prime numbers up to the given limit using the Sieve of Eratosthenes algorithm."""
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i in range(limit + 1) if is_prime[i]]

def play_round(n, primes):
    """Play one round of the game and determine the winner."""
    player_turn = 0  # 0: Maria, 1: Ben
    available_numbers = [True] * (n + 1)
    for prime in primes:
        if prime > n:
            break
        if available_numbers[prime]:
            for j in range(prime, n + 1, prime):
                available_numbers[j] = False
            player_turn = 1 - player_turn
    return "Maria" if player_turn == 1 else "Ben"

def isWinner(x, nums):
    """Determine the winner of multiple rounds."""
    if x <= 0 or not nums:
        return None
    primes = sieve_of_eratosthenes(max(nums))
    scores = {"Maria": 0, "Ben": 0}
    for n in nums:
        winner = play_round(n, primes)
        scores[winner] += 1
    if scores["Maria"] > scores["Ben"]:
        return "Maria"
    elif scores["Ben"] > scores["Maria"]:
        return "Ben"
    else:
        return None
