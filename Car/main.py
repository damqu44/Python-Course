import keyboard  # from pip
import os

redFont = '\x1b[38;2;255;0;0m'
greenFont = '\x1b[38;2;124;252;0m'


class Car:
    def __init__(self):
        self.__engine = True
        self.__gear = 1
        self.__speed = 0
        self.__acceleration = 2
        self.__brakingForce = 3

    def __startEngine(self):
        self.__engine = True

    def __stopEngine(self):
        self.__engine = False

    def __speedUp(self):
        if self.__engine == True and self.__speed < 240:
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
        else:
            exit

    def __isEngineOn(self):
        if self.__engine:
            fontColor = greenFont
            carStatus = 'on'
        else:
            fontColor = redFont
            carStatus = 'off'
        return fontColor + carStatus

    def carControl(self):
        while True:
            try:
                if keyboard.is_pressed('w'):
                    self.__speedUp()
                    self.__showParameters()
                elif keyboard.is_pressed('s'):
                    self.__slowDown()
                    self.__showParameters()
            except:
                continue

    def __showParameters(self):
        os.system('cls')
        print('\n Car status: ' + self.__isEngineOn() + '\x1b[0m')
        print('\n Car speed: ', self.__speed)
        print('\n Car gear:', self.__gear)
        if self.__engine == True and self.__speed >= 240:
            print(
                redFont + '\n The car has reached its maximum speed.' + '\x1b[0m')
        elif self.__engine == False:
            print('\n The car is off.')


car1 = Car()
car1.carControl()
