#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isnumeric():
    print("N must be a number")
    exit(1)

N = queens = int(sys.argv[1])
if N < 4:
    print("N must be at least 4")
    exit(1)


def CrossOut(Grid, cell, dimension):
    Grid[cell[0]][cell[1]][1] = 1
    # Horizontal
    for horizontal_cell in Grid[cell[0]]:
        if horizontal_cell[1] == 0:
            horizontal_cell[1] = -1
    # Vertical
    for x in range(dimension):
        vertical_cell = Grid[x][cell[1]]
        if vertical_cell[1] == 0:
            vertical_cell[1] = -1
    # Right Diagonal
    if cell[1] < dimension - 1:
        for x in range(1, dimension - cell[1]):
            try:
                grid[cell[0] + x][cell[1] + x][1] = -1
            except BaseException:
                pass
            try:
                if cell[0] - x >= 0:
                    grid[cell[0] - x][cell[1] + x][1] = -1
            except BaseException:
                pass

    # Left Diagonal
    if cell[1] > 0:
        for x in range(1, cell[1] + 1):
            try:
                if cell[1] - x >= 0:
                    grid[cell[0] + x][cell[1] - x][1] = -1
            except BaseException:
                pass
            try:
                if (cell[0] - x >= 0) and (cell[1] - x >= 0):
                    grid[cell[0] - x][cell[1] - x][1] = -1
            except BaseException:
                pass

    return grid


def GetNextSpot(grid):
    for row in range(len(grid)):
        for column in range(len(grid)):
            cell = grid[row][column]
            if cell[1] == 0:
                return [row, column]
    return None


def CountSpots(grid):
    count = 0
    for row in range(len(grid)):
        for column in range(len(grid)):
            cell = grid[row][column]
            if cell[1] == 0:
                count += 1
    return count


def print_answer(grid, N):
    result = []
    for row in range(N):
        for column in range(N):
            cell = grid[row][column]
            if cell[1] == 1:
                result.append(cell[0])
    print(result)


def print_grid(grid, N):
    for row in range(N):
        for column in range(N):
            print(grid[row][column], "\t", end="")
        print()


for row in range(N):
    grid = [[[[i, j], 0] for j in range(N)] for i in range(N)]
    flag = 0
    grid = CrossOut(grid, [0, row], N)
    queens = N - 1
    while (queens):
        if CountSpots(grid) < queens:
            flag = 1
            break
        NextSpot = GetNextSpot(grid)
        if not NextSpot:
            flag = 1
            break
        grid = CrossOut(grid, NextSpot, N)
        queens -= 1
    if not flag:
        print_answer(grid, N)
