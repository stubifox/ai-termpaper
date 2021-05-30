#!/usr/bin/env python
# coding: utf-8
start1 = {
    'data': ((13, 2, 10, 3),
             (1, 12, 8, 4),
             (5, 0, 9, 6),
             (15, 14, 11, 7)),
    'name': 'start1'}

start2 = {
    'data': ((0,  1,  2,  3),
             (4,  5,  6,  8),
             (14,  7, 11, 10),
             (9, 15, 12, 13)
             ),
    'name': 'start2'
}

start3 = {
    'data': ((6, 13, 7, 10),
             (8, 9, 11, 0),
             (15, 2, 12, 5),
             (14, 3, 1, 4)),
    'name': 'start3'
}


start4 = {
    'data': ((3, 9, 1, 15),
             (14, 11, 4, 6),
             (13, 0, 10, 12),
             (2, 7, 8, 5)),
    'name': 'start4'
}

start5 = {
    'data': ((1,  2,  3, 4),
             (5,  6,  7, 8),
             (9, 10, 11, 12),
             (13, 15, 14, 0)),
    'name': 'start5'
}

upperLeft = {
    'data': ((0, 1, 2, 3),
             (4, 5, 6, 7),
             (8, 9, 10, 11),
             (12, 13, 14, 15)),
    'name': 'solved - Blank upper Left'
}

downRight = {
    'data': ((1, 2, 3, 4),
             (5, 6, 7, 8),
             (9, 10, 11, 12),
             (13, 14, 15, 0)),
    'name': 'solved - Blank down Right'
}
upperRight = {
    'data': ((1, 2, 3, 0),
             (4, 5, 6, 7),
             (8, 9, 10, 11),
             (12, 13, 14, 15)),
    'name': 'solved - Blank upper Right'
}
downLeft = {
    'data': ((1, 2, 3, 4),
             (5, 6, 7, 8),
             (9, 10, 11, 12),
             (0, 13, 14, 15)),
    'name': 'solved - Blank down Left'
}
spirale = {
    'data': ((1, 2, 3, 4),
             (12, 13, 14, 5),
             (11, 0, 15, 6),
             (10, 9, 8, 7)),
    'name': 'spirale Goal'
}

Starts = [start1, start2, start3, start4, start5]
Goals = [upperLeft, upperRight, downLeft, downRight, spirale]


def to_1d(Puzzle: tuple) -> list:
    return [elem for tupl in Puzzle for elem in tupl]


def swap(idxA, idxB, Puzzle_1d):
    Puzzle_1d[idxA], Puzzle_1d[idxB] = Puzzle_1d[idxB], Puzzle_1d[idxA]


def find_tile_1d(tile, State_1d):
    n = len(State_1d)
    for it in range(n):
        if State_1d[it] == tile:
            return it


def get_inversion_count(Puzzle: tuple) -> int:
    working_1d_puzzle = to_1d(Puzzle)
    count = 0
    old_count = -1
    while old_count != count:
        old_count = count
        for i in range(len(working_1d_puzzle)):
            if working_1d_puzzle[i] != i:
                count += 1
                swap(i, find_tile_1d(i, working_1d_puzzle), working_1d_puzzle)
    return count


def find_tile(tile, State):
    n = len(State)
    for row in range(n):
        for col in range(n):
            if State[row][col] == tile:
                return row, col


def manhattan(stateA, stateB):
    tile = 0
    result = 0
    rowA, colA = find_tile(tile, stateA)
    rowB, colB = find_tile(tile, stateB)
    result += abs(rowA - rowB) + abs(colA - colB)
    return result


def is_solvable(Start: tuple, verbose: bool = False) -> int:
    Destination: tuple = upperLeft
    if verbose:
        print(f"Name: {Start['name']}")
        print(f"Start is: {Start['data']}")
        print(f"Inversion Count: {get_inversion_count(Start['data'])}")
        print(
            f"Manhattan Distance: {manhattan(Start['data'], Destination['data'])}")
    return (get_inversion_count(Start['data']) + manhattan(Start['data'], Destination['data'])) % 2 == 0


for s in Starts:
    print(f"is solvable: {is_solvable(s, verbose=True)}")
    print('\n')

get_inversion_count(start4['data'])
