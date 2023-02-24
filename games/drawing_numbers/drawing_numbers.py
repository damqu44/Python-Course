
import random
import os


redFont = '\x1b[38;2;255;0;0m'
greenFont = '\x1b[38;2;124;252;0m'


def printWelcomeScreen():
    print('\n Welcome!')
    print('\n Lottery game - the program draws six numbers from 1-49,')
    print('\n and the user is tasked with selecting six numbers.')
    print('\n The program displays how many numbers were matched.')
    input('\n Press enter to continue..')
    enterUserNumbers()


def drawingNumbers():
    drawnNumbers = []
    i = 1
    while i <= 6:
        drawnNumber = random.randrange(1, 49)
        if drawnNumber not in drawnNumbers:
            drawnNumbers.append(drawnNumber)
            i = i + 1
        else:
            continue
    os.system('cls')
    return drawnNumbers


def enterUserNumbers():
    drawnNumbers = drawingNumbers()
    userNumbers = []
    ordinalNumbers = ['first', 'second', 'third',
                      'forth', 'fifth', 'sixth', 'seventh']
    i = 0
    while i <= 5:
        userNumber = input(
            '\n Enter ' + ordinalNumbers[i] + ' integer number from 1 to 49: ')
        os.system('cls')
        if userNumber.isdigit():
            userNumber = int(userNumber)
            if userNumber > 0 and userNumber < 50:
                if userNumber not in userNumbers:
                    userNumbers.append(userNumber)
                    i = i + 1
                else:
                    print(
                        redFont + "\n Numbers can't be repetated." + '\x1b[0m')
                    continue
            else:
                print(
                    redFont + '\n Enter numbers only from 1 to 49.' + '\x1b[0m')
                continue
        else:
            print(redFont + '\n Enter only integer numbers.' + '\x1b[0m')
            continue
    countCorrectHits(userNumbers, drawnNumbers)


def countCorrectHits(userNumbers, drawnNumbers):
    correctHits = 0
    for x in userNumbers:
        if x in drawnNumbers:
            correctHits = correctHits + 1
    print('\n Drawn numbers:', drawnNumbers)
    print('\n Your numbers:', userNumbers)
    print(greenFont + '\n Your score is:', correctHits, '\x1b[0m')
    endGame()


def endGame():
    userMenu = input('\n Enter 1. to play again or 2. to exit: ')
    if userMenu == '1':
        enterUserNumbers()
    elif userMenu == '2':
        exit
    else:
        os.system('cls')
        endGame()


printWelcomeScreen()
