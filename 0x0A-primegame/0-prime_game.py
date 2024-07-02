#!/usr/bin/python3
"""
Pg
"""


def primeNumbers(n):
    """Return prime nums between 1 and n inc
       Args:
        n (int): upper boundary of range. lower boundary = 1
    """
    pNs = []
    ft = [True] * (n + 1)
    for prime in range(2, n + 1):
        if ft[prime]:
            pNs.append(prime)
            for gg in range(prime, n + 1, prime):
                ft[gg] = False
    return pNs


def isWinner(x, nums):
    """
    Determines the winner
    Args:
        x (int): nmbr of rounds of game
        nums (int): upper limit of range for each round
    Return:
        Name of winner (Maria or Ben) or None
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for c in range(x):
        pNs = primeNumbers(nums[c])
        if len(pNs) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
