import time
import os
from typing import List

USE_DEMO = False
USE_LOGGING = False

def getMainInput():
    file = open('DemoSource.txt', 'r') if USE_DEMO else open('Source.txt', 'r')
    input = [[int(y) for y in x.strip()] for x in file.readlines()]

    if USE_LOGGING: print(input)

    return input

def incrementGrid(inputGrid):
    for i in (range(10)):
        for j in range(10):
            inputGrid[i][j] += 1

def flashGrid(inputGrid):
    doFlashCheck = True
    flashCount = 0

    while doFlashCheck:
        doFlashCheck = False
        for i in range(10):
            for j in range(10):
                if inputGrid[i][j] > 9: # octo flash engaged
                    doFlashCheck = True
                    flashCount += 1
                    inputGrid[i][j] = 0

                    for k in range(i-1, i+2): # {i-1, i, i+1}
                        for l in range(j-1, j+2): # {j-1, j, j+1}
                            if k in range(10) and l in range(10) and inputGrid[k][l] > 0:
                                inputGrid[k][l] += 1

    return flashCount

def getFlashCount(inputGrid, stepCount):
    count = 0

    for i in range(stepCount):
        incrementGrid(inputGrid)
        count += flashGrid(inputGrid)

    return count

def getFirstAllFlash(inputGrid):
    stepCounter = 0

    while True:
        stepCounter += 1
        if USE_LOGGING: print("Processing step ", stepCounter)

        incrementGrid(inputGrid)
        if flashGrid(inputGrid) == 100: return stepCounter

os.chdir('Day 11')

startTime = time.time()

input = getMainInput()
steps = 100

#Challenge 1
#solution = getFlashCount(input, steps)

#Challenge 2
solution = getFirstAllFlash(input)

endtime = time.time()

if solution == -1: print('ERROR')

print(f'Solution: ', solution)
print('Completion time: ', endtime - startTime)