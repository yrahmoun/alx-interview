#!/usr/bin/python3
""" module for minOperations """


def minOperations(n):
    """Calculate fewest no. of operations needed to result in n H characters"""
    operations = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            operations += factor
            n /= factor
        factor += 1
    return operations
