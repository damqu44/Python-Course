import random


def drawingNumbers():
    i = 0
    global randomNumbers
    randomNumbers = []
    while i < 10:
        randomNumber = random.randint(1, 20)
        randomNumbers.append(randomNumber)
        i = i + 1


def countNumbers():
    numbersAmount = 0
    for x in randomNumbers:
        if x > 5:
            numbersAmount = numbersAmount + 1
    return numbersAmount


def countArithmeticAvg():
    arithemticAvg = 0
    for x in randomNumbers:
        if x > 5:
            arithemticAvg = arithemticAvg + x
    arithemticAvg = arithemticAvg / countNumbers()
    arithemticAvg = round(arithemticAvg, 2)
    return arithemticAvg


def countGeometricAvg():
    geometricAvg = 1
    for x in randomNumbers:
        if x > 5:
            geometricAvg = geometricAvg * x
    geometricAvg = geometricAvg ** (1/countNumbers())
    geometricAvg = round(geometricAvg, 2)
    return geometricAvg


def is_prime(n):
    for i in range(2, int(n/2)):
        if (n % i) == 0:
            return False
    return True


def countPrimeNumbers():
    primeNumbers = []
    for x in randomNumbers:
        if is_prime(x):
            primeNumbers.append(x)
    return primeNumbers


def showResults():
    print('\n Wylosowane liczby:', randomNumbers)
    print('\n Ilość liczb większych od 5:', countNumbers())
    print('\n Średnia arytmetyczna liczb większych od 5:', countArithmeticAvg())
    print('\n Średnia geometryczna liczb większych od 5:', countGeometricAvg())
    print('\n Wylosowane liczby pierwsze:', countPrimeNumbers())
    input()


drawingNumbers()
showResults()
