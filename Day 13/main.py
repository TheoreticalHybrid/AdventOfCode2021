from io import StringIO
import time
import os
from typing import List

USE_DEMO = False
USE_LOGGING = True

#DOT_GRID = []
INSTRUCTION_LIST = []


def getMainInput():
    file = open('DemoSource.txt', 'r') if USE_DEMO else open('Source.txt', 'r')
    input = [x.strip() for x in file.readlines()]

    #get max X and Y. Also fold instructions
    dotList = []

    maxX = 0
    maxY = 0
    for line in input:
        if line.startswith("fold along"): INSTRUCTION_LIST.append(line.split("fold along ")[1])
        elif line:
            #if USE_LOGGING: print(line)
            point = [int(x) for x in line.split(',')]
            dotList.append(point)
            maxX = max(maxX, point[0])
            maxY = max(maxY, point[1])

    point_grid = [[0 for x in range(maxY + 1)] for y in range(maxX + 1)]

    for point in dotList:
        point_grid[point[0]][point[1]] =1
    
    """ if USE_LOGGING: 
        print(INSTRUCTION_LIST)
        print()
        printGrid(point_grid) """

    return point_grid

def fold(instruction, pointGrid):
    inst = instruction.split('=')
    xFold = inst[0] == 'x'
    foldLine = int(inst[1])

    iRange = foldLine if xFold else len(pointGrid)
    jRange = len(pointGrid[0]) if xFold else foldLine

    newGrid = [[0 for x in range(jRange)] for y in range(iRange)]

    for i in range(iRange):
        for j in range(jRange):
            foldedI = (-1 * (i + 1)) if xFold else i
            foldedJ = j if xFold else (-1 * (j + 1))
            newGrid[i][j] = max(pointGrid[i][j], pointGrid[foldedI][foldedJ])

    return newGrid

def getPointCount(pointGrid):
    count = 0
    for i in range(len(pointGrid)):
        for j in range(len(pointGrid[0])):
            count += pointGrid[i][j]

    return count

def printGrid(pointGrid):
    for col in range(len(pointGrid[0])):
        rowStr = []
        for row in range(len(pointGrid)):
            rowStr.append('#' if pointGrid[row][col] > 0 else '.')
        print(''.join(rowStr))

os.chdir('Day 13')

startTime = time.time()

grid = getMainInput()

#Challenge 1
#if USE_LOGGING: printGrid(grid)
#grid = fold(INSTRUCTION_LIST[0], grid)
#solution = getPointCount(grid)

#Challenge 2
for instr in INSTRUCTION_LIST:
    grid = fold(instr, grid)

solution = 0

if USE_LOGGING: print()
if USE_LOGGING: printGrid(grid)

endtime = time.time()

if solution == -1: print('ERROR')

print(f'Solution: ', solution)
print('Completion time: ', endtime - startTime)