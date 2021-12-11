import time
import os
from typing import List

USE_DEMO = False
USE_LOGGING = True

def getMainInput():
    file = open('DemoSource.txt', 'r') if USE_DEMO else open('Source.txt', 'r')
    input = [int(n) for n in [x.strip() for x in file.readlines()[0].split(',')]]

    input.sort()
    if USE_LOGGING: print(input)

    return input

def getMinAdjustmentCost(inputList, maxValue, constantBurnRate = True):
    costList = [0 for i in range(maxValue + 1)]

    index = 1
    length = len(inputList)
    for crabPosition in inputList:
        if USE_LOGGING: print(f'Crab {index} of {length}')

        for i in range(maxValue + 1):
            positionChange = abs(i - crabPosition)

            fuelCost = 0

            if constantBurnRate:
                fuelCost = positionChange
            else:
                for j in range(positionChange):
                    fuelCost += 1 if constantBurnRate else (j + 1)

            costList[i] += fuelCost
        
        if USE_LOGGING: 
            if USE_DEMO: print(costList)

        index += 1

    return min(costList)

os.chdir('Day 7')

startTime = time.time()


input = getMainInput()

maxValue = input[-1]

#Challenge 1
#solution = getMinAdjustmentCost(input, maxValue)

#Challenge 2
solution = getMinAdjustmentCost(input, maxValue, False)

endtime = time.time()

print(f'Solution: ', solution)
print('Completion time: ', endtime - startTime)