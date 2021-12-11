import time
import os
from typing import List

USE_DEMO = False
USE_LOGGING = False

def getMainInput():
    file = open('DemoSource.txt', 'r') if USE_DEMO else open('Source.txt', 'r')
    input = [int(n) for n in [x.strip() for x in file.readlines()[0].split(',')]]

    if USE_LOGGING: print(input)

    return input

def getCountLookup(maxDays):
    daysCompletedCatalog = {}

    for daysLeft in range(maxDays):
        children = int(daysLeft / 7)
        if daysLeft % 7 > 0: children += 1

        count = children

        for i in range(1, children + 1):
            nextIndex = daysLeft - (7 * i) - 2
            count += daysCompletedCatalog[maxDays - nextIndex] if nextIndex > 0 else 0

        daysCompletedCatalog[maxDays - daysLeft] = count

    return daysCompletedCatalog

def calculateSchoolSize(startingSchool, waitTime):
    startingSchool.sort()
    myDict = {}

    for fish in startingSchool:
        if fish not in myDict:
            myDict[fish] = 0

        myDict[fish] += 1

    birthRateCatalog = getCountLookup(waitTime)

    schoolSize = 0
    for key in myDict:
        count = 1 + birthRateCatalog[key]
        schoolSize += count * myDict[key]
        
    return schoolSize

os.chdir('Day 6')

startTime = time.time()

startingFish = getMainInput()

#Challenge 1
#solution = calculateSchoolSize(startingFish, 80)

#Challenge 2
solution = calculateSchoolSize(startingFish, 256)

endtime = time.time()

print(f'Solution: ', solution)
print('Completion time: ', endtime - startTime)