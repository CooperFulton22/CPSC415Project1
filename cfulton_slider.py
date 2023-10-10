#!/usr/bin/env python3

'''
CPSC 415 -- Homework #2.667 template
Cooper Fulton, University of Mary Washington, fall 2023
'''

from puzzle import Puzzle
from copy import deepcopy
import numpy as np
import sys

def h1(puzzle):
    tilesNotRight = 0
    count = 1
    for x in puzzle.grid:
        for y in x:
            if y != count:
                tilesNotRight = tilesNotRight + 1
            count = count + 1
    print(tilesNotRight, " is here")
    return tilesNotRight
    

def solve(p):
    '''Finds a sequence of moves ("L", "U", "R", or "D") that will solve the
    Puzzle object passed. Returns that sequence in a list.
    '''
    # THIS IS WHERE YOUR AMAZING CODE GOES
    puzzleSolved = False
    frontier = ()
    frontierEstimates = {(), 0}
    frontierPuzzles = {(), ("deepcopy(p)")}
    while puzzleSolved == False:
        if (h1(p) == 0):
            puzzleSolved = True
    


    # Here's a (bogus) example return value:
    return ["D", "U", "L", "L"]



if __name__ == '__main__':

    if (len(sys.argv) not in [2,3]  or
        not sys.argv[1].isnumeric()  or
        len(sys.argv) == 3 and not sys.argv[2].startswith("seed=")):
        sys.exit("Usage: puzzle.py dimensionOfPuzzle [seed=###].")

    n = int(sys.argv[1])

    if len(sys.argv) == 3:
        seed = int(sys.argv[2][5:])
    else:
        seed = 123

    # Create a random puzzle of the appropriate size and solve it.
    puzzle = Puzzle.gen_random_puzzle(n, seed)
    print(puzzle)
    solution = solve(puzzle)
    if puzzle.has_solution(solution):
        input("Yay, this puzzle is solved! Press Enter to watch.")
        puzzle.verify_visually(solution)
    else:
        print(f"Sorry, {''.join(solution)} does not solve this puzzle.")
