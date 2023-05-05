#!/usr/bin/python3
""" Script that computes a minimum operations
    needed in a CopyAll - Paste task
"""


def minOperations(n):
     """
    Method for compute the minimum number
    of operations for task Copy All and Paste

    Args:
        n: input value
        factor_list: List to save the operations
    Return: the sum of the operations
    """
    if n <= 0:
        return -1  # Impossible to achieve
    ops = 0
    d = 2  # Start by copying one H and pasting it
    while n > 1:
        while n % d == 0:
            ops += d
            n //= d
        d += 1
        if d*d > n:
            ops += n
            break
    return ops
