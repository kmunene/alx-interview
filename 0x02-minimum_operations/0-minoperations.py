#!/usr/bin/python3
"""minimum operations"""


def minOperations(n: int) -> int:
    """minimum operations in a file"""
    if n <= 0:
        return 0

    operator = 0
    divider = 2

    while n > 1:
        while n % divider == 0:
            operator += divider
            n //= divider

        divider += 1

    return operator
