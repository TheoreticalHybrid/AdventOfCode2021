import time
import os

class Position:    
    def __init__(self, horizontal, depth):
        self.HorizontalPosition = horizontal
        self.Depth = depth

def getMainInput(useDemoSource = False, useLogging = False):
    file = open('DemoSource.txt', 'r') if useDemoSource else open('Source.txt', 'r')
    input = [x.split() for x in file.readlines()]

    if useLogging: print(input)

    return input

def getBasicPosition(input):
    horizontal = 0
    depth = 0

    for move in input:
        if move[0] == "forward":
            horizontal += int(move[1])
        else:
            depth += int(move[1])*(1 if move[0] == "down" else -1)

    return Position(horizontal, depth)

def getAdvancedPosition(input):
    horizontal = 0
    depth = 0
    aim = 0

    for move in input:
        if move[0] == "forward":
            horizontal += int(move[1])
            depth += int(move[1])*aim
        else:
            aim += int(move[1])*(1 if move[0] == "down" else -1)

    return Position(horizontal, depth)

os.chdir('Day 2')

useDemo = False
useLogging = False

startTime = time.time()

lines = getMainInput(useDemo, useLogging)

#Challenge 1
#position = getBasicPosition(lines)

#Challenge 2
position = getAdvancedPosition(lines)

solution = position.HorizontalPosition * position.Depth
endtime = time.time()

print(f'Solution: ', solution)
print('Completion time: ', endtime - startTime)