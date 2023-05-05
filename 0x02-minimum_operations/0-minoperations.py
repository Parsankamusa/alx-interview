#!/usr/bin/python3
""" Script that computes a minimum operations
    needed in a CopyAll - Paste task
"""


def minOperations(n):
    if n < 2:
        return 0
    list_factor = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                list_factor.append(i)
    return sum(list_factor)
