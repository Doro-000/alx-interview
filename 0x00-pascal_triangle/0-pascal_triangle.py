#!/usr/bin/python3

"""
<<<<<<< HEAD
    pascals triangle
=======
	implementation of pascals triangle
>>>>>>> 1e2032e51b4b42180a5d31b798d9fac49898b215
"""


def pascal_triangle(n):
    """
            returns a list of lists representing pascals triangle
    """
    if (n <= 0):
        return []
    triangle = [[1]]
    for i in range(n - 1):
        row = []
        for j in range(len(triangle[i]) + 1):
            if (j - 1 < 0):
                row.append(triangle[i][j])
            elif (j == len(triangle[i])):
                row.append(triangle[i][j - 1])
            else:
                row.append(triangle[i][j] + triangle[i][j - 1])
        triangle.append(row)
    return triangle
