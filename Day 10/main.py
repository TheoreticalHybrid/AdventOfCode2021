import time
import os
from typing import List

USE_DEMO = False
USE_LOGGING = False

MATCHING_CHUNKS = {
    "(" : ")",
    "[" : "]",
    "{" : "}",
    "<" : ">"
}

SYNTAX_ERROR_SCORES = {
    ")" : 3,
    "]" : 57,
    "}" : 1197,
    ">" : 25137
}

AUTOCOMPLETE_SCORES = {
    ")" : 1,
    "]" : 2,
    "}" : 3,
    ">" : 4
}

def getMainInput():
    file = open('DemoSource.txt', 'r') if USE_DEMO else open('Source.txt', 'r')
    input = [x.strip() for x in file.readlines()]

    if USE_LOGGING: print(input)

    return input

def getSyntaxScore(input):
    syntaxScore = 0    

    for line in input:
        stack = []

        for c in line:
            if c in MATCHING_CHUNKS: 
                stack.append(c)
            else:
                topChar = stack.pop()
                if MATCHING_CHUNKS[topChar] != c:
                    syntaxScore += SYNTAX_ERROR_SCORES[c]
                    break

    return syntaxScore

def getLineScore(line):
    stack = []
    score = 0

    for c in line:
        if c in MATCHING_CHUNKS: 
            stack.append(c)
        else:
            topChar = stack.pop()
            if MATCHING_CHUNKS[topChar] != c: return -1
                
    while len(stack) > 0:
        hangingChar = stack.pop()
        autoChar = MATCHING_CHUNKS[hangingChar]
        score = (score * 5) + AUTOCOMPLETE_SCORES[autoChar]

    return score

def getAutoCompleteScore(input):
    completionScores = []

    for line in input:
        score = getLineScore(line)
        if score != -1: completionScores.append(score)

    completionScores.sort()

    return completionScores[int(len(completionScores) / 2)]


os.chdir('Day 10')

startTime = time.time()

input = getMainInput()

#Challenge 1
#solution = getSyntaxScore(input)

#Challenge 2
solution = getAutoCompleteScore(input)

endtime = time.time()

if solution == -1: print('ERROR')

print(f'Solution: ', solution)
print('Completion time: ', endtime - startTime)