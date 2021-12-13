import time
import os
from typing import List

class Panel:    
    def __init__(self):
        self.Connections = []
        self.Displays = []

USE_DEMO = False
USE_LOGGING = False

ONE_DISPLAY_LENGTH = 2
FOUR_DISPLAY_LENGTH = 4
SEVEN_DISPLAY_LENGTH = 3
EIGHT_DISPLAY_LENGTH = 7

# Need to figure out how the incoming strings map to the below display diagram

#  AAAA
# B    C
# B    C
#  DDDD
# E    F
# E    F
#  GGGG

def getMainInput():
    file = open('DemoSource.txt', 'r') if USE_DEMO else open('Source.txt', 'r')
    input = [x.split(" | ") for x in file.readlines()]

    panelList = []

    for line in input:
        newPanel = Panel()

        for connection in line[0].split():
            newPanel.Connections.append(sortString(connection.strip()))

        for display in line[1].split():
            newPanel.Displays.append(sortString(display.strip()))

        panelList.append(newPanel)

        if USE_LOGGING:
            print(" ".join(newPanel.Connections), " | ", " ".join(newPanel.Displays))


    return panelList

def sortString(input):
    return "".join(sorted(input))

def getUniqueOutputCount(panelList: List[Panel]):
    count = 0

    uniqueDisplayLengths = [ONE_DISPLAY_LENGTH, FOUR_DISPLAY_LENGTH, SEVEN_DISPLAY_LENGTH, EIGHT_DISPLAY_LENGTH]

    for p in panelList:
        for display in p.Displays:
            if len(display) in uniqueDisplayLengths: count += 1
    
    return count

#Only one connection has this definition length
def get1Connection(panel: Panel):
    for c in panel.Connections:
        if len(c) == ONE_DISPLAY_LENGTH: 
            panel.Connections.remove(c)
            return c

#Only one connection has this definition length
def get4Connection(panel: Panel):
    for c in panel.Connections:
        if (len(c)) == FOUR_DISPLAY_LENGTH: 
            panel.Connections.remove(c)
            return c

#Only one connection has this definition length
def get7Connection(panel: Panel):
    for c in panel.Connections:
        if (len(c)) == SEVEN_DISPLAY_LENGTH: 
            panel.Connections.remove(c)
            return c

#Only one connection has this definition length
def get8Connection(panel: Panel):
    for c in panel.Connections:
        if (len(c)) == EIGHT_DISPLAY_LENGTH: 
            panel.Connections.remove(c)
            return c

#the A mapping is in the 7 display but not the 1 display
def getACharacter(sevenDisplay, oneDisplay):
    for c in sevenDisplay:
        if c not in oneDisplay: return c

#the F mapping is in the 1 display and in every 6 digit display
def getFCharacter(oneDisplay, panel: Panel):
    for c in oneDisplay:
        if len(list(filter(lambda conn: len(conn) == 6 and c in conn, panel.Connections))) == 3: return c

#the 6 display connection is the only 6 digit display connection without the C character
def get6Connection(panel: Panel, cCharacter):
    sixConn = list(filter(lambda conn: len(conn) == 6 and cCharacter not in conn, panel.Connections))[0]
    panel.Connections.remove(sixConn)
    return sixConn

#the D mapping is in the 4 display and in every 5 digit display
def getDCharacter(panel: Panel, fourDisplay):
    for c in fourDisplay:
        if len(list(filter(lambda conn: len(conn) == 5 and c in conn, panel.Connections))) == 3: return c

#the 0 display is the only 6 digit display without the D character
def get0Connection(panel: Panel, dCharacter):
    zeroConn = list(filter(lambda conn: len(conn) == 6 and dCharacter not in conn, panel.Connections))[0]
    panel.Connections.remove(zeroConn)
    return zeroConn

#the 9 panel is the only 6 digit display remaining
def get9Connection(panel: Panel):
    nineConn = list(filter(lambda conn: len(conn) == 6, panel.Connections))[0]
    panel.Connections.remove(nineConn)
    return nineConn

#the E mapping is the only character in 8 but not in 9
def getECharacter(eightDisplay, nineDisplay):
    for c in eightDisplay:
        if c not in nineDisplay: return c

#the B mapping is the character in 4 that isn't the C, D or F character
def getBCharacter(fourDisplay, cCharacter, dCharacter, fCharacter):
    exclusionString = cCharacter + dCharacter + fCharacter
    for c in fourDisplay:
        if c not in exclusionString: return c

#the G mapping is the character that's in 9 but not in 4, and is not the A character
def getGCharacter(nineDisplay, fourDisplay, aCharacter):
    for c in nineDisplay:
        if c != aCharacter and c not in fourDisplay: return c

def checkDisplay(translation, discoveredTranslations, panel: Panel):
    for i in range(len(discoveredTranslations)):
        for j in range(4):
            if panel.Displays[j] == discoveredTranslations[i]: translation[j] = i

    return len(list(filter(lambda d: d >= 0, translation))) == 4 # return true if each translation has been completed

def getTranslatedValue(translation):
    value = 0
    translation.reverse()
    for i in range(4):
        value += (int(translation[i]) * pow(10, i))

    return value

def getDisplayValue(panel: Panel):
    fullDisplayTranslation = [-1 for i in range(4)]

    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    individualDisplays = ["" for i in range(10)]
    individualDisplays[1] = get1Connection(panel)
    individualDisplays[4] = get4Connection(panel)
    individualDisplays[7] = get7Connection(panel)
    individualDisplays[8] = get8Connection(panel)
    if checkDisplay(fullDisplayTranslation, individualDisplays, panel):
        print('Completed at checkpoint 1')
        return getTranslatedValue(fullDisplayTranslation)

    A_map = getACharacter(individualDisplays[7], individualDisplays[1])
    F_map = getFCharacter(individualDisplays[1], panel)
    C_map = individualDisplays[1].replace(F_map, '') #the C map is the character in the 1 display that's not the F map
    
    individualDisplays[6] = get6Connection(panel, C_map)
    if checkDisplay(fullDisplayTranslation, individualDisplays, panel):
        print('Completed at checkpoint 2')
        return getTranslatedValue(fullDisplayTranslation)

    D_map = getDCharacter(panel, individualDisplays[4])
    individualDisplays[0] = get0Connection(panel, D_map)
    individualDisplays[9] = get9Connection(panel)
    if checkDisplay(fullDisplayTranslation, individualDisplays, panel):
        print('Completed at checkpoint 3')
        return getTranslatedValue(fullDisplayTranslation)

    E_map = getECharacter(individualDisplays[8], individualDisplays[9])
    B_map = getBCharacter(individualDisplays[4], C_map, D_map, F_map)
    G_map = getGCharacter(individualDisplays[9], individualDisplays[4], A_map)

    individualDisplays[2] = sortString("".join([A_map, C_map, D_map, E_map, G_map]))
    individualDisplays[3] = sortString("".join([A_map, C_map, D_map, F_map, G_map]))
    individualDisplays[5] = sortString("".join([A_map, B_map, D_map, F_map, G_map]))
    if checkDisplay(fullDisplayTranslation, individualDisplays, panel):
        print('Completed at checkpoint 4')
        return getTranslatedValue(fullDisplayTranslation)

    return -1 #this should never be reached


def getDisplaySum(panelList: List[Panel]):
    sum = 0

    for p in panelList:
        displayVal = getDisplayValue(p)
        if displayVal == -1: return -1

        sum += displayVal

    return sum

os.chdir('Day 8')

startTime = time.time()


input = getMainInput()

#Challenge 1
#solution = getUniqueOutputCount(input)

#Challenge 2
solution = getDisplaySum(input)

endtime = time.time()

if solution == -1: print('ERROR')

print(f'Solution: ', solution)
print('Completion time: ', endtime - startTime)