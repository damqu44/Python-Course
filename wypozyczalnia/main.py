from datetime import date
from datetime import timedelta
import os
import json


redFont = '\x1b[38;2;255;0;0m'
greenFont = '\x1b[38;2;124;252;0m'
yellowFont = '\x1b[38;2;255;255;0m'

with open('C:/Users/Damian/Desktop/Python/wypozyczalnia/file.json') as file:
    json_dict = json.load(file)


class Customer:
    def __init__(self, id, name, lastname, getDrivingLicenseData):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.getDrivingLicenseData = getDrivingLicenseData


class Car:
    def __init__(self, id, brand, segment, fuelType, pricePerDay, status):
        self.id = id
        self.brand = brand
        self.segment = segment
        self.fuelType = fuelType
        self.pricePerDay = pricePerDay
        self.status = status


def showMenu():
    print('\n Options menu:')
    print('\n List of customers and cars: 1')
    print('\n Rental a car: 2')
    print('\n Exit the program: 3')
    userInputMenu = input('\n\n Enter 1, 2 or 3: ')
    if userInputMenu == '1':
        os.system('cls')
        showLists()
    elif userInputMenu == '2':
        os.system('cls')
        rentalCar()
    elif userInputMenu == '3':
        exit
    else:
        os.system('cls')
        showMenu()


def showLists():
    printCustomersList()
    printCarsList()
    showMenu()


def generateLists():
    generateCustomersList()
    generateCarsList()


def generateCustomersList():
    global customersList
    customersList = []
    for x in json_dict['customers']:
        client = Customer(x['id'], x['name'], x['lastname'],
                          x['getDrivingLicenseData'])
        customersList.append(client)


def generateCarsList():
    global carsList
    carsList = []
    for x in json_dict['cars']:
        car = Car(x['id'], x['brand'], x['segment'],
                  x['fuelType'], x['pricePerDay'], x['status'])
        carsList.append(car)


def printCustomersList():
    text = '{0:5s}{1:25s}{2:25s}'
    print('\n Clients List:')
    print('\n ------------------------')
    print(text.format('\n ' + 'Id', 'Name and lastname', 'Driving license issue date'))
    for x in customersList:
        print(text.format('\n ' + x.id, x.name + " " +
              x.lastname, x.getDrivingLicenseData))
    print('\n ------------------------')


def printCarsList():
    text = '{0:5s}{1:25s}{2:15s}{3:15s}{4:10s}'
    print('\n Cars List:')
    print('\n ------------------------')
    print(text.format('\n ' + 'Id', 'Brand',
          'Segment', 'Fuel Type', 'Price Per Day'))
    for x in carsList:
        print(text.format('\n ' + x.id, x.brand,
              x.segment, x.fuelType, x.pricePerDay))
    print('\n ------------------------')


def rentalCar():
    global intClientId
    clientId = input('\n Please, enter client ID: ')
    clientId = str(clientId)

    for x in customersList:
        if clientId in x.id:
            idCheck = True
            break
        else:
            idCheck = False
    if idCheck:
        os.system('cls')
        intClientId = int(clientId)
        segmentMenu()
    else:
        os.system('cls')
        print(
            redFont + 'Customer with the given ID not found.' + '\x1b[0m')
        rentalCar()


def segmentMenu():
    print('\n Choose segment.')
    print('\n 1. mini')
    print('\n 2. compact')
    print('\n 3. premium')
    global segmentInput
    segmentInput = input('\n Enter 1, 2 or 3: ')
    if segmentInput == '1' or segmentInput == '2' or segmentInput == '3':
        os.system('cls')
        fuelTypeMenu()
    else:
        os.system('cls')
        segmentMenu()


def fuelTypeMenu():

    print('\n Choose fuel type.')
    print('\n 1. petrol')
    print('\n 2. electric')
    print('\n 3. diesel')
    global fuelTypeInput
    fuelTypeInput = input('\n Enter 1, 2 or 3: ')
    if fuelTypeInput == '1' or fuelTypeInput == '2' or fuelTypeInput == '3':
        if carsList[intClientId-1].status == 'available':
            os.system('cls')
            rentalLength()
        else:
            os.system('cls')
            print(
                redFont + '\n Sorry, Currently there are no vehicles that match the criteria.' + '\x1b[0m')
            showMenu()
    else:
        os.system('cls')
        fuelTypeMenu()


def rentalLength():
    daysAmount = input('\n Enter the number of days of renting the vehicle: ')
    if daysAmount.isdigit():
        daysAmount = int(daysAmount)
        if daysAmount > 0 and daysAmount < 31:
            os.system('cls')
            generateContract(daysAmount)
        else:
            os.system('cls')
            print(
                redFont + 'The maximum rental period is 30 days.' + '\x1b[0m')
            rentalLength()
    else:
        os.system('cls')
        rentalLength()


def generateContract(daysAmount):
    price = carsList[intClientId-1].pricePerDay
    price = price.split(' ', 1)
    price[0] = int(price[0])
    print(yellowFont + '\n Vehicle rental agreement')
    print('\n Date of conclusion:', date.today(), '\x1b[0m')
    print('\n ------------------------------------------')
    print(yellowFont + '\n Tenant: ' +
          customersList[intClientId-1].name + customersList[intClientId-1].lastname)
    print('\n Vehicle brand: ' + carsList[intClientId-1].brand)
    print('\n Fuel Type: ' + carsList[intClientId-1].fuelType)
    print('\n Segment: ' + carsList[intClientId-1].segment + '\x1b[0m')
    print('\n ------------------------------------------')
    print(yellowFont + '\n Vehicle return date:',
          date.today() + timedelta(days=daysAmount))
    print('\n Fee:', price[0]*daysAmount, price[1], '\x1b[0m')
    print('\n ------------------------------------------')
    confirmation = input('\n Do you accept the agreement? (Y/N): ')
    confirmation = confirmation.upper()
    if confirmation == 'Y' or confirmation == 'YES':
        os.system('cls')
        print(greenFont + '\n You have successfully rented ' +
              carsList[intClientId-1].brand + ' for', daysAmount, 'days.' + '\x1b[0m')
        carsList[intClientId-1].status = 'unavailable'
        showMenu()
    elif confirmation == 'N' or confirmation == 'NO':
        os.system('cls')
        print(redFont + '\n You have denied ' +
              carsList[intClientId-1].brand + ' rental.')
        print('\n The contract has been cancelled \x1b[0m')
        showMenu()
    else:
        os.system('cls')
        print(redFont + '\n Enter yes or no... \x1b[0m')
        generateContract(daysAmount)


print('\n Welcome to car rental.\n')
generateLists()
showMenu()
