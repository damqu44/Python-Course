'''
Lottery game - the program draws six numbers from 1-49,
and the user is tasked with selecting six numbers.
The program displays how many numbers were matched.
'''

import os
import random


def drawingNumbers():
    drawnNumbers = []
    i = 1
    while i <= 6:
        drawnNumber = random.randrange(1, 7)
        if drawnNumber not in drawnNumbers:
            drawnNumbers.append(drawnNumber)
            i = i + 1
        else:
            continue
    os.system('cls')
    print(drawnNumbers)
    enterUserNumbers()


def enterUserNumbers():
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
            if userNumber > 1 and userNumber < 50:
                if userNumber not in userNumbers:
                    userNumbers.append(userNumber)
                    i = i + 1
                else:
                    print("\n Numbers can't be repetated.")
                    continue
            else:
                print('\n Enter numbers only from 1 to 49.')
                continue
        else:
            print('\n Enter only integer numbers.')
            continue
    print(userNumbers)


drawingNumbers()
