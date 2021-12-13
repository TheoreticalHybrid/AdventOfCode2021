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

def getRiskLevel(heightmap):
    gridHeight = len(heightmap)
    gridWidth = len(heightmap[0])
    
    riskLevel = 0    

    for r in range(gridHeight):
        for c in range(gridWidth):
            myHeight = heightmap[r][c]

            #up
            if (r-1) >= 0:
                if heightmap[r-1][c] <= myHeight: continue

            #down
            if (r+1) < gridHeight:
                if heightmap[r+1][c] <= myHeight: continue

            #left
            if (c-1) >= 0:
                if heightmap[r][c-1] <= myHeight: continue

            #right
            if (c+1) < gridWidth:
                if heightmap[r][c+1] <= myHeight: continue

            #if this point has been reached, it's a low point
            riskLevel += myHeight + 1

    return riskLevel

def buildBasinMap(heightMap, basinMap, row, col):
    basinMap[row][col] = 1
    size = 1

     #up
    if (row-1) >= 0:
        if heightMap[row-1][col] < 9 and basinMap[row-1][col] == 0: 
            size += buildBasinMap(heightMap, basinMap, row-1, col)

    #down
    if (row+1) < len(heightMap):
        if heightMap[row+1][col] < 9 and basinMap[row+1][col] == 0: 
            size += buildBasinMap(heightMap, basinMap, row+1, col)

    #left
    if (col-1) >= 0:
        if heightMap[row][col-1] < 9 and basinMap[row][col-1] == 0: 
            size += buildBasinMap(heightMap, basinMap, row, col-1)

    #right
    if (col+1) < len(heightMap[0]):
        if heightMap[row][col+1] < 9 and basinMap[row][col+1] == 0: 
            size += buildBasinMap(heightMap, basinMap, row, col+1)

    return size


def getBasinSize(heightmap, row, col):
    basinMap = [[0 for i in range(len(heightmap[0]))] for j in range(len(heightmap))]

    return buildBasinMap(heightmap, basinMap, row, col)


def getBasinScore(heightmap):
    gridHeight = len(heightmap)
    gridWidth = len(heightmap[0])
    
    top3Sizes = [0 for i in range(3)]

    for r in range(gridHeight):
        for c in range(gridWidth):
            myHeight = heightmap[r][c]

            #up
            if (r-1) >= 0:
                if heightmap[r-1][c] <= myHeight: continue

            #down
            if (r+1) < gridHeight:
                if heightmap[r+1][c] <= myHeight: continue

            #left
            if (c-1) >= 0:
                if heightmap[r][c-1] <= myHeight: continue

            #right
            if (c+1) < gridWidth:
                if heightmap[r][c+1] <= myHeight: continue

            #if this point has been reached, it's a low point
            basinSize = getBasinSize(heightmap, r, c)
            top3Sizes.append(basinSize)
            top3Sizes = sorted(top3Sizes, reverse=True)[:3]

    product = 1
    for size in top3Sizes:
        product = product * size

    return product

os.chdir('Day 09')

startTime = time.time()

input = getMainInput()

#Challenge 1
#solution = getRiskLevel(input)

#Challenge 2
solution = getBasinScore(input)

endtime = time.time()

if solution == -1: print('ERROR')

print(f'Solution: ', solution)
print('Completion time: ', endtime - startTime)