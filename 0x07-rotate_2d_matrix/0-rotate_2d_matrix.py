#!/usr/bin/python3

"""
rotation(transpose) of a 2d matrix
"""

from sqlalchemy import PrimaryKeyConstraint


def rotate_2d_matrix(matrix):
    """
    implementation
    """
    reverse = list(reversed([row[:] for row in matrix]))
    for row in range(len(matrix)):
        for column in range(len(matrix)):
            matrix[row][column] = reverse[column][row]
