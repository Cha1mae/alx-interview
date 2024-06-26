#!/usr/bin/python3
""" min op to reach 4"""


def minOperations(n):
    if n <= 1:
        return 0
    n_o = 0
    d = 2
    while n > 1:
        while n % d == 0:
            n_o += d
            n //= d
        d += 1
    return n_o
