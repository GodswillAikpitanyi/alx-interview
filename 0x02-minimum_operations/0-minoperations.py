#!/usr/bin/python3
"""Calculate the minimum operation required for a task to occur"""


import math


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in
    exactly n 'H' characters.

    Args:
        n (int): The desired number of 'H' characters.

    Returns:
        int: The fewest number of operations needed to
            achieve n 'H' characters.
             If n is impossible to achieve, return 0.
    """

    if n <= 1:
        return 0

    operations = 0
    # Find the prime factorization of n
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            operations += i
            n //= i

    # If n is still greater than 1, it is a prime factor itself
    if n > 1:
        operations += n

    return operations
