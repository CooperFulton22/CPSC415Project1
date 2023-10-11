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
    #print(tilesNotRight, " is here")
    return tilesNotRight

def insert_into_frontier(frontier, frontierEstimates, sequence, cost):
    spotFound = False
    for x in frontier:
        print("here")
        print(x)
        if frontierEstimates[x] > cost:
            frontier.insert(sequence)
            spotFound = True

    if spotFound == False:
        frontier.append(sequence)

    return frontier

def solve(p):
    '''Finds a sequence of moves ("L", "U", "R", or "D") that will solve the
    Puzzle object passed. Returns that sequence in a list.
    '''
    # THIS IS WHERE YOUR AMAZING CODE GOES
    frontier = [()]
    frontierEstimates = {(): 0}
    frontierPuzzles = {(): deepcopy(p)}
    puzzleSolved = False
    count = 0
    while count < 11:
        poppedFrontier = frontier[0]
        frontier.pop(0)
        legalMovesAtState = frontierPuzzles[poppedFrontier].legal_moves()
        print(legalMovesAtState)
        for x in legalMovesAtState:
            moveToAdd = x
            newFrontier = poppedFrontier + (moveToAdd,)
            print("newFrontier is", newFrontier)
            print("moveToAdd is", moveToAdd)
            estToAdd = h1(frontierPuzzles[poppedFrontier])
            print("estToAdd is", estToAdd)
            puzzlePulled = frontierPuzzles[poppedFrontier]
            print("puzzlePulled is\n", puzzlePulled)
            if puzzlePulled.is_solved() == True:
                sequenceReturn = poppedFrontier
            copyOfMove = deepcopy(puzzlePulled)
            copyOfMove.move(moveToAdd)
            print("copyOfMove is", copyOfMove)
            h1ToAdd = h1(copyOfMove)
            estToAdd = h1ToAdd
            alreadyInPuzzles = False
            for y in frontierPuzzles.values():
                print("y is", y)
                print("copyOfMove now is\n", copyOfMove)
                if y == copyOfMove:
                    alreadyInPuzzles = True
            if alreadyInPuzzles == False:
                print("insert being called")
                frontierPuzzles[newFrontier] = copyOfMove
                print("frontierPuzzles is now", frontierPuzzles)
                frontierEstimates[newFrontier] = estToAdd
                print("frontierEstimates is now", frontierEstimates)
                print("frontier before call is", frontier)
                frontier = insert_into_frontier(frontier, frontierEstimates, newFrontier, estToAdd)
                print(frontier) 
        count = count + 1
        if (h1ToAdd == 0):
            puzzleSolved = True
    


    # Here's a (bogus) example return value:
    return poppedFrontier



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
