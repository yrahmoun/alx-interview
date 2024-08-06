#!/usr/bin/python3
"""module for task 0"""


def isWinner(x, nums):
    """Determine the winner of the Prime Game"""
    if x <= 0 or not nums:
        return None
    max_n = max(nums)
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False

    def count_primes(n):
        """Count the number of prime numbers"""
        count = 0
        for i in range(1, n + 1):
            if is_prime[i]:
                count += 1
        return count
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if count_primes(n) % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
