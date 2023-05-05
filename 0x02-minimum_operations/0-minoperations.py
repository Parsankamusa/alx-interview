#!/usr/bin/python3
""" Script that computes a minimum operations
    needed in a CopyAll - Paste task
"""


def minOperations(n):
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
