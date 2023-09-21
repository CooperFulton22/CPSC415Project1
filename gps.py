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
    totalCost = 0
    pathList = [0]
    checkDistanceList = []
    checkRoadList = []
    numCities = atlas.get_num_cities()
    cityCheckingWith = 0
    cityIncrement = 0
    shortestRoad = 0
    cityToAdd = 0
    if alg == "Dijkstras":
        findingGoalState = True
        while findingGoalState == True:
            while cityIncrement < numCities:
                if (atlas.get_road_dist(cityCheckingWith, cityIncrement) != math.inf and atlas.get_road_dist(cityCheckingWith, cityIncrement) != 0):
                    checkDistanceList.append(atlas.get_road_dist(cityCheckingWith, cityIncrement))
                    shortestRoad = atlas.get_road_dist(cityCheckingWith, cityIncrement)
                    checkRoadList.append(cityIncrement);
                    cityIncrement = cityIncrement + 1
                else:
                    cityIncrement = cityIncrement + 1
            spotInDistanceList = 0
            for road in checkDistanceList:
                if road < shortestRoad:
                    shortestRoad = road
            
            #finding spot in list for city to add
            goThroughList = True
            while goThroughList == True:
                if checkDistanceList[spotInDistanceList] == shortestRoad:
                    cityToAdd = checkRoadList[spotInDistanceList]
                    goThroughList = False
                elif spotInDistanceList == len(checkRoadList):
                    goThroughList = False
                else:
                    spotInDistanceList = spotInDistanceList + 1

            #add to total cost and add to final list to be returned
            totalCost = totalCost + shortestRoad
            pathList.append(cityToAdd)
            cityCheckingWith = cityToAdd
            checkDistanceList.clear()
            checkRoadList.clear()
            cityIncrement = 0
            shortestRoad = 0
            
            #if goal state is found, end
            if cityToAdd == numCities - 1:
                findingGoalState = False
            else:
                cityToAdd = 0
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

