#!/usr/bin/python3
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

    while primes and primes[0] <= n:  # Continue while there are primes to be removed
        prime = primes.pop(0)  # Select the smallest available prime
        numbers = [num for num in numbers if num % prime != 0]  # Remove multiples of the prime
        player_turn = "Maria" if player_turn == "Ben" else "Ben"  # Switch turns between Maria and Ben

    winner = "Maria" if player_turn == "Ben" else "Ben"  # Determine the winner
    return winner

def isWinner(x, nums):
    """Determine the winner of the prime game after x rounds.
    
    Args:
        x (int): The number of rounds to be played.
        nums (list): A list containing the upper limit for each round.
    
    Returns:
        str: The name of the player that won the most rounds ("Maria" or "Ben"), or None if it's a tie.
    """
    if x <= 0 or not nums:  # Check if input is valid
        return None

    primes = sieve_of_eratosthenes(max(nums))  # Generate prime numbers up to the maximum number in the rounds
    scores = {"Maria": 0, "Ben": 0}  # Track the number of rounds each player wins

    for n in nums:  # For each round
        winner = play_round(n, primes[:])  # Determine the winner for the round
        scores[winner] += 1  # Update the score for the winner

    if scores["Maria"] > scores["Ben"]:  # Determine the overall winner
        return "Maria"
    elif scores["Ben"] > scores["Maria"]:
        return "Ben"
    else:
        return None
