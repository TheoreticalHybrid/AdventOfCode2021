from io import StringIO
import time
import os
from typing import List

USE_DEMO = False
USE_LOGGING = True

STARTING_CAVE_ID = "start"
ENDING_CAVE_ID = "end"
COMPLETED_PATH_LIST = []

class Cave:
    def __init__(self, id, smallCave):
        self.Id = id
        self.SmallCave = smallCave
        self.LinkedCaves = {}

    def LinkCave(self, cave):
        if cave.Id not in self.LinkedCaves:
            self.LinkedCaves[cave.Id] = cave


def getMainInput():
    file = open('DemoSource.txt', 'r') if USE_DEMO else open('Source.txt', 'r')
    
    startingCave = Cave(STARTING_CAVE_ID, True)
    endingCave = Cave(ENDING_CAVE_ID, True)

    caveDictionary = {
        STARTING_CAVE_ID : startingCave,
        ENDING_CAVE_ID : endingCave
    }
    
    for line in file.readlines():
        caveLinkage = line.split("-")
        
        caveId1 = caveLinkage[0].strip()
        cave1 = None
        if caveId1 == STARTING_CAVE_ID: cave1 = startingCave
        elif caveId1 == ENDING_CAVE_ID: cave1 = endingCave
        elif caveId1 in caveDictionary: cave1 = caveDictionary[caveId1]
        else: 
            cave1 = Cave(caveId1, caveId1.islower())
            caveDictionary[caveId1] = cave1

        caveId2 = caveLinkage[1].strip()
        cave2 = None
        if caveId2 == STARTING_CAVE_ID: cave2 = startingCave
        elif caveId2 == ENDING_CAVE_ID: cave2 = endingCave
        elif caveId2 in caveDictionary: cave2 = caveDictionary[caveId2]
        else: 
            cave2 = Cave(caveId2, caveId2.islower())
            caveDictionary[caveId2] = cave2

        cave1.LinkCave(cave2)
        cave2.LinkCave(cave1)

    if USE_LOGGING:
        for key in caveDictionary:
            print("Key: ", key)
            cave = caveDictionary[key]
            print("Cave Id: ", cave.Id)
            print("Small Cave: ", "True" if cave.SmallCave else "False")
            print("Linked Caves: ", [key for key in cave.LinkedCaves])

    return startingCave

def findAllPaths(cave: Cave, pathList: List[str]):
    if cave.SmallCave and cave.Id in pathList: 
        return #can't visit small caves more than once
    else:
        pathList.append(cave.Id) #add my cave to the path
    
    if cave.Id == ENDING_CAVE_ID:
        pathString = ",".join(pathList)
        
        if pathString not in COMPLETED_PATH_LIST:
            COMPLETED_PATH_LIST.append(pathString)

        pathList.pop()
        return

    for key in cave.LinkedCaves:
        findAllPaths(cave.LinkedCaves[key], pathList)

    pathList.pop() #remove my cave from the path

def findAllPaths2(cave: Cave, pathList: List[str]):
    if cave.SmallCave and cave.Id in pathList: 
        #can only visit a single small cave twice, all other small caves only once

        #start can still only be hit once
        if cave.Id == STARTING_CAVE_ID: return

        smallCaveList = []
        for caveId in pathList:
            if not caveId.islower(): continue
            elif caveId not in smallCaveList: smallCaveList.append(caveId)
            else: return #already found an instance where we've hit a small cave twice, can't continue with this path

        #if it reaches past the for loop, then no small cave has been visited twice and this cave can be visited again
    
    pathList.append(cave.Id) #add my cave to the path

    if USE_LOGGING: print(",".join(pathList))
    
    if cave.Id == ENDING_CAVE_ID:
        pathString = ",".join(pathList)
        
        if pathString not in COMPLETED_PATH_LIST:
            COMPLETED_PATH_LIST.append(pathString)
            if USE_LOGGING: print(pathString, " COMPLETE!")

        pathList.pop()
        return

    for key in cave.LinkedCaves:
        findAllPaths2(cave.LinkedCaves[key], pathList)

    pathList.pop() #remove my cave from the path
        

os.chdir('Day 12')

startTime = time.time()

startingCave = getMainInput()
pathList = []

#Challenge 1
#findAllPaths(startingCave, pathList)

#Challenge 2
findAllPaths2(startingCave, pathList)

solution = len(COMPLETED_PATH_LIST)
if USE_LOGGING:
    print("Completed Paths")
    for path in COMPLETED_PATH_LIST:
        print(path)

endtime = time.time()

if solution == -1: print('ERROR')

print(f'Solution: ', solution)
print('Completion time: ', endtime - startTime)