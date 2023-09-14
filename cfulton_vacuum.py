'''
CPSC 415 -- Program #1 support file
Stephen Davies, University of Mary Washington, fall 2023
'''

import logging
import sys
import random

from vacuum import VacuumAgent
from agent import *
from environment import *



class CfultonVacuumAgent(VacuumAgent):
    image_filename = 'cleaner.gif'
    possible_actions = ['Right', 'Left', 'Up', 'Down', 'Suck', 'NoOp']
    def __init__(self):
        super().__init__()
        self._bump = False
        self.coordsVisited = []
        #x and y both start at 0, (0,0) being the starting point
        self.x = 0
        self.y = 0
        self.coordAt = (self.x, self.y)
        self.coordsVisited.append(self.coordAt)
        self.lastAction = ""
        self.noOpCount = 0
        self.noOpAction = False
        self.actionAfterNoOpCycleEnds = ""
        self.spinCycle = 0
    def program(self, percept):
        if (percept[0] == 'Dirty'):
            return 'Suck'
        else:
            if self.noOpCount == 5 and self.noOpAction == True and (self.actionAfterNoOpCycleEnds == "" or self.actionAfterNoOpCycleEnds == "Left"):
                self.spinCycle = self.spinCycle + 1
                if self.spinCycle % 4 == 0 and self.spinCycle > 0:
                    self.spinCycle = self.spinCycle - 4
                    return 'Up'
                else:
                    self.noOpCount = 0
                    self.noOpAction = False
                    self.lastAction = "Up"
                    self.actionAfterNoOpCycleEnds = "Up"
                    self.y = self.y + 1
                    self.coordAt = (self.x, self.y)
                    return 'Up'
            elif self.noOpCount == 5 and self.noOpAction == True and self.actionAfterNoOpCycleEnds == "Up":
                self.spinCycle = self.spinCycle + 1
                if self.spinCycle % 4 == 0 and self.spinCycle > 0:
                    self.spinCycle = self.spinCycle - 4
                    return 'Right'
                else:
                    self.noOpCount = 0
                    self.spinCycle = self.spinCycle + 1
                    self.noOpAction = False
                    self.lastAction = "Right"
                    self.actionAfterNoOpCycleEnds = "Right"
                    self.x = self.x + 1
                    self.coordAt = (self.x, self.y)
                    return 'Right'
            elif self.noOpCount == 5 and self.noOpAction == True and self.actionAfterNoOpCycleEnds == "Right":
                self.spinCycle = self.spinCycle + 1
                if self.spinCycle % 4 == 0 and self.spinCycle > 0:
                    self.spinCycle = self.spinCycle - 4
                    return 'Down'
                else:
                    self.noOpCount = 0
                    self.spinCycle = self.spinCycle + 1
                    self.noOpAction = False
                    self.lastAction = "Down"
                    self.actionAfterNoOpCycleEnds = "Down"
                    self.y = self.y - 1
                    self.coordAt = (self.x, self.y)
                    return 'Down'
            elif self.noOpCount == 5 and self.noOpAction == True and self.actionAfterNoOpCycleEnds == "Down":
                self.spinCycle = self.spinCycle + 1
                if self.spinCycle % 4 == 0 and self.spinCycle > 0:
                    self.spinCycle = self.spinCycle - 4
                    return 'Left'
                else:
                    self.noOpCount = 0
                    self.spinCycle = self.spinCycle + 1
                    self.noOpAction = False
                    self.lastAction = "Left"
                    self.actionAfterNoOpCycleEnds = "Left"
                    self.x = self.x - 1
                    self.coordAt = (self.x, self.y)
                    return 'Left'
            elif percept[1] == 'None' and self.lastAction == "" :
                self.lastAction = "Up"
                self.y = self.y + 1
                self.coordAt = (self.x, self.y)
                self.coordsVisited.append(self.coordAt)
                #print(self.coordsVisited)
                return 'Up'
            elif percept[1] == 'None' and self.lastAction == "Up":
                self.lastAction = "Up"
                self.y = self.y + 1
                self.coordAt = (self.x, self.y)
                found = False
                for coord in self.coordsVisited:
                    if coord == self.coordAt:
                        found = True
                        self.lastAction = "Right"
                        self.y = self.y - 1
                        self.coordAt = (self.x, self.y)
                        self.noOpCount = self.noOpCount + 1
                        self.noOpAction = True
                        return 'NoOp'
                        break
                if found == False:
                    self.noOpAction = False
                    self.coordsVisited.append(self.coordAt)
                    #print(self.coordsVisited)
                    return 'Up'
            elif percept[1] == 'Bump' and self.lastAction == "Up":
                self.lastAction = "Right"
                self.x = self.x + 1
                self.y = self.y - 1
                self.coordAt = (self.x, self.y)
                found = False
                for coord in self.coordsVisited:
                    if coord == self.coordAt:
                        found = True
                        self.lastAction = "Right"
                        self.x = self.x - 1
                        self.coordAt = (self.x, self.y)
                        self.noOpCount = self.noOpCount + 1
                        self.noOpAction = True
                        return 'NoOp'
                        break
                if found == False:
                    self.noOpAction = False
                    self.coordsVisited.append(self.coordAt)
                    #print(self.coordsVisited)
                    return 'Right'
            elif percept[1] == 'None' and self.lastAction == "Right":
                self.lastAction = "Right"
                self.x = self.x + 1
                self.coordAt = (self.x, self.y)
                found = False
                for coord in self.coordsVisited:
                    if coord == self.coordAt:
                        found = True
                        self.lastAction = "Down"
                        self.x = self.x - 1
                        self.coordAt = (self.x, self.y)
                        self.noOpCount = self.noOpCount + 1
                        self.noOpAction = True
                        return 'NoOp'
                        break
                if found == False:
                    self.noOpAction = False
                    self.coordsVisited.append(self.coordAt)
                    #print(self.coordsVisited)
                    return 'Right'
            elif percept[1] == 'Bump' and self.lastAction == "Right":
                self.lastAction = "Down"
                self.y = self.y - 1
                self.x = self.x - 1
                self.coordAt = (self.x, self.y)
                found = False
                for coord in self.coordsVisited:
                    if coord == self.coordAt:
                        found = True
                        self.lastAction = "Down"
                        self.y = self.y + 1
                        self.coordAt = (self.x, self.y)
                        self.noOpCount = self.noOpCount + 1
                        self.noOpAction = True
                        return 'NoOp'
                        break
                if found == False:
                    self.noOpAction = False
                    self.coordsVisited.append(self.coordAt)
                    #print(self.coordsVisited)
                    return 'Down'
            elif percept[1] == 'None' and self.lastAction == "Down":
                self.lastAction = "Down"
                self.y = self.y - 1
                self.coordAt = (self.x, self.y)
                found = False
                for coord in self.coordsVisited:
                    if coord == self.coordAt:
                        found = True
                        self.lastAction = "Left"
                        self.y = self.y + 1
                        self.coordAt = (self.x, self.y)
                        self.noOpCount = self.noOpCount + 1
                        self.noOpAction = True
                        return 'NoOp'
                        break
                if found == False:
                    self.noOpAction = False
                    self.coordsVisited.append(self.coordAt)
                    #print(self.coordsVisited)
                    return 'Down'
            elif percept[1] == 'Bump' and self.lastAction == "Down":
                self.lastAction = "Left"
                self.x = self.x - 1
                self.y = self.y + 1
                self.coordAt = (self.x, self.y)
                found = False
                for coord in self.coordsVisited:
                    if coord == self.coordAt:
                        found = True
                        self.lastAction = "Left"
                        self.x = self.x + 1
                        self.coordAt = (self.x, self.y)
                        self.noOpCount = self.noOpCount + 1
                        self.noOpAction = True
                        return 'NoOp'
                        break
                if found == False:
                    self.noOpAction = False
                    self.coordsVisited.append(self.coordAt)
                    #print(self.coordsVisited)
                    return 'Left'
            elif percept[1] == 'None' and self.lastAction == "Left":
                self.lastAction = "Left"
                self.x = self.x - 1
                self.coordAt = (self.x, self.y)
                found = False
                for coord in self.coordsVisited:
                    if coord == self.coordAt:
                        found = True
                        self.lastAction = "Up"
                        self.x = self.x + 1
                        self.coordAt = (self.x, self.y)
                        self.noOpCount = self.noOpCount + 1
                        self.noOpAction = True
                        return 'NoOp'
                        break
                if found == False:
                    self.noOpAction = False
                    self.coordsVisited.append(self.coordAt)
                    #print(self.coordsVisited)
                    return 'Left'
            elif percept[1] == 'Bump' and self.lastAction == "Left":
                self.lastAction = "Up"
                self.y = self.y + 1
                self.x = self.x + 1
                self.coordAt = (self.x, self.y)
                found = False
                for coord in self.coordsVisited:
                    if coord == self.coordAt:
                        found = True
                        self.lastAction = "Up"
                        self.y = self.y - 1
                        self.coordAt = (self.x, self.y)
                        self.noOpCount = self.noOpCount + 1
                        self.noOpAction = True
                        return 'NoOp'
                        break
                if found == False:
                    self.noOpAction = False
                    self.coordsVisited.append(self.coordAt)
                    #print(self.coordsVisited)
                    return 'Up'
            
class VacuumEnvironment(XYEnvironment):

    """The environment of [Ex. 2.12]. Agent perceives dirty or clean, and bump
    (into obstacle) or not; 2D discrete world of unknown size; performance
    measure is 80 for each square of dirt cleaned, -10 for each 'suck' action,
    and -3 for each move action."""

    def __init__(self, width=10, height=10):
        super().__init__(width, height)
        self.add_walls()

    def thing_classes(self):
        return [Wall, Dirt, ReflexVacuumAgent, RandomVacuumAgent,
                TableDrivenVacuumAgent, ModelBasedVacuumAgent]

    def percept(self, agent):
        """The percept is a tuple of ('Dirty' or 'Clean', 'Bump' or 'None').
        Unlike the TrivialVacuumEnvironment, location is NOT perceived."""
        status = ('Dirty' if self.some_things_at(
            self[agent], Dirt) else 'Clean')
        bump = ('Bump' if agent._bump else 'None')
        return (status, bump)

    def execute_action(self, agent, action):
        if action not in agent.possible_actions:
            print("Illegal action {}! Shutting down.".format(action))
            sys.exit(1)
        if action == 'Suck':
            agent.performance -= 10
            dirt_list = self.list_things_at(self[agent], Dirt)
            if dirt_list != []:
                dirt = dirt_list[0]
                agent.performance += 80
                self.delete_thing(dirt)
        else:
            super().execute_action(agent, action)

        if action in {'Left','Right','Up','Down'}:
            agent.performance -= 3

    def is_clean(self):
        return all([ type(thing) is not Dirt for thing in self ])

    def should_shutdown(self):
        return self.is_clean()

    def add_to_random_empty_square(self, thing):
        possible_squares = [(x,y) for x in range(self.width) 
            for y in range(self.height) if (x,y) not in self.values()]
        self.add_thing(thing,random.choice(possible_squares))
        

class DirtyVacuumEnvironment(VacuumEnvironment):

    def __init__(self, width=10, height=10, dirt_prob=.5):
        super().__init__(width, height)
        self.width=width
        self.height=height
        self.dirt_prob=dirt_prob
        self._scatter_dirt()

    def _scatter_object(self, cls, prob=.5):
        '''Randomly put down an object of the class passed on every empty 
        square, with probability passed.'''
        possible_squares = [(x,y) for x in range(self.width) 
            for y in range(self.height) if (x,y) not in self.values()]
        for sq in possible_squares:
            if random.random() < prob:
                self.add_thing(cls(), sq)

    def _scatter_dirt(self):
        self._scatter_object(Dirt, self.dirt_prob)


class RandomDirtyVacuumEnvironment(DirtyVacuumEnvironment):

    def __init__(self, width_range=(10,20), height_range=(10,20)):
        super().__init__(
            random.randint(*width_range), random.randint(*height_range))
        self._add_walls()

    def _add_walls(self):
        self._scatter_object(Wall, .2)



class Dirt(Thing):
    image_filename = 'dirt.gif'
