import time
import os

def getMainInput(useDemoSource = False, useLogging = False):
    file = open('DemoSource.txt', 'r') if useDemoSource else open('Source.txt', 'r')
    input = [int(x) for x in file.readlines()]

    if useLogging: print(input)

    return input

def getNumberOfDepthIncreases(input):
    count = 0
    for i in range(len(input) - 1):
        if input[i+1] > input[i]: count += 1

    return count

def getNumberOfDepthWindowIncreases(input):
    count = 0

    for i in range(3, len(input)):
        window1 = input[i-3] + input[i-2] + input[i-1]
        window2 = input[i-2] + input[i-1] + input[i]

        if window2 > window1: count += 1

    return count

os.chdir('Day 01')

useDemo = False
useLogging = False

startTime = time.time()

lines = getMainInput(useDemo)

#Challenge 1
#solution = getNumberOfDepthIncreases(lines)

#Challenge 2
solution = getNumberOfDepthWindowIncreases(lines)

endtime = time.time()

print(f'Solution: ', solution)