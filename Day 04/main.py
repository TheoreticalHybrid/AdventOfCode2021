import time
import os

class BingoNight:    
    def __init__(self):
        self.Instructions = []
        self.Cards = []

MARK_VAL = 'X'
USE_DEMO = False
USE_LOGGING = False

def getMainInput():
    file = open('DemoSource.txt', 'r') if USE_DEMO else open('Source.txt', 'r')
    input = file.readlines()

    bingo = BingoNight()
    bingo.Instructions = [x.strip() for x in input[0].split(',')]

    for i in range(2, len(input) - 4, 6):
        card = []

        for j in range(5):
            card.append([x.strip() for x in input[i+j].split()])

        bingo.Cards.append(card)

    if USE_LOGGING: 
        print(bingo.Instructions)
        print(bingo.Cards)

    return bingo

def markCard(card, value):
    for rowIndex in range(5):
        for colIndex in range(5):
            if card[rowIndex][colIndex] == value:
                card[rowIndex][colIndex] = MARK_VAL

                #check for row bingo
                rowCompleted = True
                for c in range(5):
                    rowCompleted &= card[rowIndex][c] == MARK_VAL

                if rowCompleted: return True

                #check for column bingo
                colCompleted = True
                for r in range(5):
                    colCompleted &= card[r][colIndex] == MARK_VAL

                if colCompleted: return True

    return False

def getCardValue(card):
    value = 0
    for row in card:
        for col in row:
            if col != MARK_VAL: value += int(col)

    return value

def playBingo(bingoNight, findLosingCard = False):
    instructions = bingoNight.Instructions
    cards = bingoNight.Cards

    lastWinningValue = 0

    for calledNumber in instructions:
        completedCards = []
        for card in cards:
            bingoAchieved = markCard(card, calledNumber)

            if bingoAchieved:
                if USE_LOGGING: 
                    print(f'Last Called Number: {calledNumber}')
                    
                    for row in card:
                        print(row)

                lastWinningValue = getCardValue(card) * int(calledNumber)

                if findLosingCard:
                    completedCards.append(card)
                else:
                    break
        else:
            for card in completedCards:
                cards.remove(card)
            continue

        break

    return lastWinningValue

os.chdir('Day 04')

startTime = time.time()

bingo = getMainInput()

#Challenge 1
#solution = playBingo(bingo)

#Challenge 2
solution = playBingo(bingo, True)

endtime = time.time()

print(f'Solution: ', solution)
print('Completion time: ', endtime - startTime)