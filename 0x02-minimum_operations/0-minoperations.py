#!/usr/bin/python3
""" min op to reach 4"""


def minOperations(n):
    if n <= 1:
        return 0
    n_o = 0
    p = 2
    while n > 1:
        while n % p == 0:
            n_o += p
            n //= p
        p += 1
    return n_o
