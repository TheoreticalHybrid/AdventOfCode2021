import time
import os
from typing import List

class Point:
    def __init__(self, xValue: int, yValue: int):
        self.XValue = xValue
        self.YValue = yValue

class VentLine:    
    def __init__(self, startPoint: Point, endPoint: Point):
        self.StartPoint = startPoint
        self.EndPoint = endPoint

USE_DEMO = False
USE_LOGGING = False

def getMainInput():
    file = open('DemoSource.txt', 'r') if USE_DEMO else open('Source.txt', 'r')
    input = [[[int(z.strip()) for z in y.split(',')] for y in x.split(" -> ")] for x in file.readlines()]

    #if USE_LOGGING: print(input)

    ventLines = []

    for instruction in input:
        point1 = Point(instruction[0][0], instruction[0][1])
        point2 = Point(instruction[1][0], instruction[1][1])
        ventLines.append(VentLine(point1, point2))

    """ if USE_LOGGING:
        for vl in ventLines:
            print(f'{vl.StartPoint.XValue},{vl.StartPoint.YValue} -> {vl.EndPoint.XValue},{vl.EndPoint.YValue}') """

    return ventLines

def getMap(input: List[VentLine]):
    maxX = 0
    maxY = 0
    for vl in input:
        maxX = max(maxX, vl.StartPoint.XValue, vl.EndPoint.XValue)
        maxY = max(maxY, vl.StartPoint.YValue, vl.EndPoint.YValue)

    return [[0] * (maxX + 1) for _ in range(maxY + 1)]

def markMapLine(myMap, point1: Point, point2: Point, basicMode):
    if point1.XValue == point2.XValue:
        minY = min(point1.YValue, point2.YValue)
        maxY = max(point1.YValue, point2.YValue)
        
        for y in range(minY, maxY + 1):
            myMap[point1.XValue][y] += 1

    elif point1.YValue == point2.YValue:
        minX = min(point1.XValue, point2.XValue)
        maxX = max(point1.XValue, point2.XValue)
        
        for x in range(minX, maxX + 1):
            myMap[x][point1.YValue] += 1
            
    elif not basicMode:
        if USE_LOGGING: print(f'{point1.XValue},{point1.YValue} -> {point2.XValue},{point2.YValue}')

        for i in range(abs(point1.XValue - point2.XValue) + 1):
            thisX = point1.XValue + (i * (1 if point1.XValue < point2.XValue else -1))
            thisY = point1.YValue + (i * (1 if point1.YValue < point2.YValue else -1))

            if USE_LOGGING: print(f'Marking {thisX},{thisY}')

            myMap[thisX][thisY] += 1

def buildMap(input: List[VentLine], map, basicMode = True):
    for vl in input:
        markMapLine(map, vl.StartPoint, vl.EndPoint, basicMode)

    if USE_LOGGING:
        for row in map:
            print(''.join([str(c) for c in row]))

    count = 0
    for row in map:
        for col in row:
            if col > 1: count += 1

    return count


os.chdir('Day 5')

startTime = time.time()

lines = getMainInput()
map = getMap(lines)


#Challenge 1
#solution = buildMap(lines, map)

#Challenge 2
solution = buildMap(lines, map, False)

endtime = time.time()

print(f'Solution: ', solution)
print('Completion time: ', endtime - startTime)