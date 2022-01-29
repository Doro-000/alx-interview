#!/usr/bin/python3

"""
Minimum Operations
"""


def minOperations(n):
    """
    implementation
    """
    if n <= 0:
        return 0

    operations, letters, clipboard = 0, 1, 0
    while (letters != n):
        if (n % letters == 0):
            operations += 2
            clipboard = letters
        else:
            operations += 1
        letters += clipboard
    return operations
