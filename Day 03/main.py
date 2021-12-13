import time
import os

def getMainInput(useDemoSource = False, useLogging = False):
    file = open('DemoSource.txt', 'r') if useDemoSource else open('Source.txt', 'r')
    input = [x.strip() for x in file.readlines()]

    if useLogging: print(input)

    return input

def getPowerConsumption(input):

    totals = [0]*len(input[0])

    for line in input:
        for i in range(len(line)):
            totals[i] += int(line[i])

    gammaValue = 0
    epsilonValue = 0
    totals.reverse()
    for i in range(len(totals)):
        if totals[i] > (len(input)/2):
            gammaValue += pow(2, i)
        else:
            epsilonValue += pow(2, i)

    return gammaValue*epsilonValue

def getO2Rating(input):
    remainingInput = input
    
    for i in range(len(remainingInput[0])):
        if len(remainingInput) == 1: break

        count = 0
        for line in remainingInput:
            count += int(line[i])

        remainingInput = list(filter(lambda x: x[i] == ("1" if count >= (len(remainingInput)/2) else "0"), remainingInput))

    return remainingInput[0]

def getCO2Rating(input):
    remainingInput = input
    
    for i in range(len(remainingInput[0])):
        if len(remainingInput) == 1: break

        count = 0
        for line in remainingInput:
            count += int(line[i])

        remainingInput = list(filter(lambda x: x[i] == ("0" if count >= (len(remainingInput)/2) else "1"), remainingInput))

    return remainingInput[0]

def convertBinaryStringToDecimal(input):
    input = input[::-1]

    value = 0
    for i in range(len(input)):
        value += int(input[i]) * pow(2, i)

    return value


def getLifeSupportRating(input):
    o2Rating = getO2Rating(input)
    co2Rating = getCO2Rating(input)

    return convertBinaryStringToDecimal(o2Rating) * convertBinaryStringToDecimal(co2Rating)

os.chdir('Day 03')

useDemo = False
useLogging = False

startTime = time.time()

lines = getMainInput(useDemo, useLogging)

#Challenge 1
#solution = getPowerConsumption(lines)

#Challenge 2
solution = getLifeSupportRating(lines)

endtime = time.time()

print(f'Solution: ', solution)
print('Completion time: ', endtime - startTime)