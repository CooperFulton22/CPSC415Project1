#!/usr/bin/env python3

'''
CPSC 415 -- Homework #2
Cooper Fulton, University of Mary Washington, fall 2023
'''

from atlas import Atlas
import numpy as np
import sys
import math


def find_path(atlas, alg):
    '''Finds a path from src to dest using a specified algorithm, and
    based on costs from the atlas provided. The second argument must be one
    of the values "greedy", "Dijkstras", or "A*".

    Returns a tuple of two elements. The first is a list of city numbers,
    starting with 0 and ending with atlas.num_cities-1, that gives the
    optimal path between those two cities. The second is the total cost
    of that path.'''

    # THIS IS WHERE YOUR AMAZING CODE GOES
    #Amazing code!
    # Here's a (bogus) example return value:

    #initialize variables
    totalCost = 0
    pathList = [0]
    queueStack = []
    nodesExpanded = [0]
    numCities = atlas.get_num_cities()
    cityCheckingWith = 0
    cityIncrement = 0
    addedDistance = 0
    dictOfPaths = {0: [0]}
    #for Dijkstras
    if alg == "Dijkstras":
        findingGoalState = True
        #all occurs while finding goal state (numcities - 1)
        while findingGoalState == True:
            #adding cities with distances to list and distances respectively
            while cityIncrement < numCities:
                #print(atlas.get_road_dist(cityCheckingWith, cityIncrement))
                #print("\n")
                if (atlas.get_road_dist(cityCheckingWith, cityIncrement) != math.inf and atlas.get_road_dist(cityCheckingWith, cityIncrement) != 0):
                    if cityIncrement not in queueStack and cityIncrement not in nodesExpanded:
                        tup = (atlas.get_road_dist(cityCheckingWith, cityIncrement) + addedDistance, cityIncrement)
                        queueStack.append(tup)
                        cityIncrement = cityIncrement + 1
                    else:
                        cityIncrement = cityIncrement + 1
                else:
                    cityIncrement = cityIncrement + 1
            #order queueToStack to put shortest g(n) in front and then order them
            queueStack.sort(key=lambda a: a[0])
            print(queueStack)
            if dictOfPaths.get(cityCheckingWith) == [cityCheckingWith]:
                dictOfPaths[queueStack[0][-1]] = dictOfPaths.get(cityCheckingWith)
                print(dictOfPaths)
                #print(dictOfPaths.get(queueStack[0][-1]), "is here")
                #print(queueStack[0][-1])
                dictOfPaths.get(queueStack[0][-1]).append(queueStack[0][-1])
                print(dictOfPaths)
            #print(dictOfPaths)
            cityCheckingWith = queueStack[0][-1]
            #print("City check is ", cityCheckingWith)
            addedDistance = queueStack[0][0]
            tup2 = (cityCheckingWith, addedDistance)
            nodesExpanded.append(tup2)
            #print("Nodes expanded ", nodesExpanded)
            queueStack.pop(0)

            
            '''
            #add to total cost and add to final list to be returned
            totalCost = totalCost + shortestRoad
            pathList.append(cityToAdd)
            print(cityToAdd)
            '''
            #reinitialize variables for next go around
            cityIncrement = 0
            if (cityCheckingWith == numCities - 1):
                findingGoalState = False
                totalCost = addedDistance
                 
            #if goal state is found, end
             
    return (pathList, totalCost)



if __name__ == '__main__':

    if len(sys.argv) != 3:
        print("Usage: gps.py numCities|atlasFile algorithm.")
        sys.exit(1)

    if len(sys.argv) > 2:
        if sys.argv[2] not in ['greedy', 'Dijkstras', 'A*']:
            print(f'Algorithm must be one of: "greedy", "Dijkstras", or "A*".'
                f' (You put "{sys.argv[2]}".)')
            sys.exit(2)
        else:
            alg = sys.argv[2]

    try:
        num_cities = int(sys.argv[1])
        print(f'Building random atlas with {num_cities} cities...')
        usa = Atlas(num_cities)
        print('...built.')
    except:
        print(f'Loading atlas from file {sys.argv[1]}')
        usa = Atlas.from_filename(sys.argv[1])
        print('...loaded.')

    path, cost = find_path(usa, alg)
    print(f'The {alg} path from 0 to {usa.get_num_cities()-1}'
        f' costs {cost}: {path}.')
    ne = usa._nodes_expanded
    print(f'It expanded {len(ne)} nodes: {ne}')

