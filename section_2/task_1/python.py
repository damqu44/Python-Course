import os


def is_float_digit_v2(n: str) -> bool:
    return n.replace('.', '', 1).isdigit()


def wrongValue():
    os.system('cls')
    print('\n You typed wrong. Enter a key to return to menu.')
    input()
    os.system('cls')
    showMenu()


def backToMenu():
    print('\n\n Enter a key to return to menu.')
    input()
    os.system('cls')
    showMenu()


def convertDegreesToFahrenheit():
    print('\n You have selected the Celsius to Fahrenheit converter. ')
    userInputCelsius = input('\n Enter the temperature in Celsius: ')
    if is_float_digit_v2(userInputCelsius):
        userInputCelsius = float(userInputCelsius)
        celsiusInFahrenheit = round(32 + (9/5)*userInputCelsius, 2)
        print('\n', userInputCelsius, 'C is', celsiusInFahrenheit, 'F')
        backToMenu()
        input()
    else:
        wrongValue()


def convertDegreesToKelvin():
    print('\n You have selected the Celsius to Kelvin converter. ')
    userInputCelsius = input('\n Enter the temperature in Celsius: ')
    if is_float_digit_v2(userInputCelsius):
        userInputCelsius = float(userInputCelsius)
        celsiusInKelvin = round(userInputCelsius + 273.15, 2)
        print('\n', userInputCelsius, 'C is', celsiusInKelvin, 'K')
        backToMenu()
        input()
    else:
        wrongValue()


def algorithm():
    print('\n You have selected algorithm that always return 2, let see for yourself.')
    userNumberOne = input('\n Enter the first number other than zero: ')
    userNumberTwo = input('\n Enter the second number other than zero: ')
    userNumberOne = float(userNumberOne)
    userNumberTwo = float(userNumberTwo)
    userNumber = userNumberOne + userNumberTwo
    userNumber = ((((userNumber * userNumber) - (userNumberOne *
                  userNumberOne)) - (userNumberTwo * userNumberTwo)) / userNumberOne) / userNumberTwo
    userNumber = round(userNumber, 1)
    print(userNumber)
    input()


def showMenu():
    print('\n 1. Convert degrees Celsius to Fahrenheit.')
    print('\n 2. Convert degrees Celsius to Kelvin.')
    print('\n 3. Check algorithm.')
    print('\n 4. Exit the program.')
    userInputMenu = input('\n Choose 1, 2, 3 or 4: ')
    if userInputMenu == '1':
        os.system('cls')
        convertDegreesToFahrenheit()
    elif userInputMenu == '2':
        os.system('cls')
        convertDegreesToKelvin()
    elif userInputMenu == '3':
        os.system('cls')
        algorithm()
    elif userInputMenu == '4':
        exit
    else:
        os.system('cls')
        showMenu()


showMenu()
