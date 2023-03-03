import keyboard  # from pip
import os
import json
import time

redFont = '\x1b[38;2;255;0;0m'
greenFont = '\x1b[38;2;124;252;0m'

with open('C:/Users/Damian/Desktop/Python/car/file.json') as file:
    json_dict = json.load(file)


class Car:
    def __init__(self, id, brand, __acceleration, __brakingForce, __maxSpeed):
        self.id = id
        self.brand = brand
        self.__acceleration = __acceleration
        self.__brakingForce = __brakingForce
        self.__maxSpeed = __maxSpeed
        self.__engine = False
        self.__gear = 1
        self.__speed = 0

    def __startEngine(self):
        self.__engine = True

    def __stopEngine(self):
        self.__engine = False

    def __speedUp(self):
        if self.__engine == True and self.__speed < self.__maxSpeed:
            self.__speed = self.__speed + self.__acceleration
            self.__speed = round(self.__speed, 1)
            self.__automaticGearbox()

    def __slowDown(self):
        if self.__engine == True and self.__speed > 0:
            self.__speed = self.__speed - self.__brakingForce
            if self.__speed < 0:
                self.__speed = 0
            else:
                self.__speed = round(self.__speed, 1)
            self.__automaticGearbox()

    def __automaticGearbox(self):
        if self.__speed <= 19:
            self.__gear = 1
        elif self.__speed >= 20 and self.__speed <= 39:
            self.__gear = 2
        elif self.__speed >= 30 and self.__speed <= 49:
            self.__gear = 3
        elif self.__speed >= 50 and self.__speed <= 89:
            self.__gear = 4
        elif self.__speed >= 90 and self.__speed <= 129:
            self.__gear = 5
        elif self.__speed >= 130 and self.__speed:
            self.__gear = 6

    def __isEngineOn(self):
        if self.__engine:
            fontColor = greenFont
            carStatus = 'on'
        else:
            fontColor = redFont
            carStatus = 'off'
        return fontColor + carStatus

    def carControl(self):
        self.__showParameters()
        while True:
            try:
                if keyboard.is_pressed('w'):
                    self.__speedUp()
                    self.__showParameters()
                elif keyboard.is_pressed('s'):
                    self.__slowDown()
                    self.__showParameters()
                elif keyboard.is_pressed('t'):
                    if self.__speed == 0:
                        if self.__engine == True:
                            self.__stopEngine()
                            self.__showParameters()
                            time.sleep(1)
                        else:
                            self.__startEngine()
                            self.__showParameters()
                            time.sleep(1)
                elif keyboard.is_pressed('e'):
                    if self.__engine == False:
                        break
            except:
                continue

    def __showParameters(self):
        os.system('cls')
        print('\n ------------------------')
        print('\n Car: ' + self.brand)
        print('\n Car status: ' + self.__isEngineOn() + '\x1b[0m')
        print('\n Car speed:', self.__speed, 'km/h')
        print('\n Car gear:', self.__gear)
        if self.__engine == True and self.__speed >= self.__maxSpeed:
            print(
                redFont + '\n The car has reached its maximum speed.' + '\x1b[0m')
        print('\n ------------------------')
        print('\n Keys Menu:')
        print('\n T - turn on/off')
        print('\n W - speed up')
        print('\n S - slow down')
        print('\n E - change car')
        print('\n ------------------------')


def generateCarsList():
    global carsList
    carsList = []
    for x in json_dict['cars']:
        car = Car(x['id'], x['brand'], x['acceleration'],
                  x['brakingForce'], x['maxSpeed'])
        carsList.append(car)


def printCarList():
    text = '{0:5s}{1:25s}'
    print('\n Cars List:')
    print('\n ------------------------')
    print(text.format('\n ' + 'Id', 'Brand'))
    for x in carsList:
        print(text.format('\n ' + x.id, x.brand))
    print('\n ------------------------')


def chooseCar():
    os.system('cls')
    printCarList()
    carChoosen = input('\n Enter number of a car: ')
    if carChoosen.isdigit():
        carChoosen = int(carChoosen)
        if carChoosen > 0 and carChoosen < len(carsList)+1:
            return carChoosen
        else:
            chooseCar()
    else:
        chooseCar()


def makingCarObject():
    selectedCar = carsList[chooseCar()-1]
    return selectedCar


generateCarsList()

while True:
    try:
        makingCarObject().carControl()
    except:
        exit()
