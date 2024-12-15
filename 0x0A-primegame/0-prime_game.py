#!/usr/bin/python3
"""Module for Prime Game"""

def sieve_of_eratosthenes(limit):
 """Function to get who has won in prime game"""

    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
                
    primes = [i for i in range(limit + 1) if is_prime[i]]
    return primes

def play_round(n, primes):
    player_turn = "Maria"
    numbers = list(range(1, n + 1))

    while primes and primes[0] <= n:
        prime = primes.pop(0)
        numbers = [num for num in numbers if num % prime != 0]
        player_turn = "Maria" if player_turn == "Ben" else "Ben"

    winner = "Maria" if player_turn == "Ben" else "Ben"
    return winner

def isWinner(x, nums):
    if x <= 0 or not nums:
        return None

    primes = sieve_of_eratosthenes(max(nums))
    scores = {"Maria": 0, "Ben": 0}

    for n in nums:
        winner = play_round(n, primes[:])
        scores[winner] += 1

    if scores["Maria"] > scores["Ben"]:
        return "Maria"
    elif scores["Ben"] > scores["Maria"]:
        return "Ben"
    else:
        return None
