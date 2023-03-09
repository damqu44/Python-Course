import json
import os

redFont = '\x1b[38;2;255;0;0m'
greenFont = '\x1b[38;2;124;252;0m'
orangeFont = '\x1b[38;2;255;165;0m'
cEnd = '\x1b[0m'

filePath = 'C:/Users/Damian/Desktop/Python/reg&login-decorators/file.json'
usersList = []


class Network():
    __users = []
    __authorized = False
    __email = None
    __password = None
    __name = None
    __lastname = None

    def authorize(self):
        login = input('\n E-mail: ')
        password = input('\n Password: ')
        os.system('cls')
        with open(filePath, "r") as file:
            json_dict = json.load(file)
            for x in json_dict['users']:
                if x['email'] == login:
                    self.__email = x['email']
                    self.__password = x['password']
                    self.__name = x['name']
                    self.__lastname = x['lastname']
        if login == self.__email and password == self.__password:
            print(greenFont + '\n Authorized!' + cEnd)
            return True
        else:
            print(redFont + '\n Not authorized!' + cEnd)
            return False

    def notlogged(func):
        def innerFunc(self, *args, **kwargs):
            if self.__authorized == True:
                return
            else:
                return func(self, *args, **kwargs)

        return innerFunc

    def logged(func):

        def innerFunc(self, *args, **kwargs):
            if self.__authorized == False:
                return
            else:
                return func(self, *args, **kwargs)

        return innerFunc

    @logged
    def display(self, list):
        text = '{0:5s}{1:10s}{2:15s}'
        print(text.format('\n', 'Name', 'Last name\n'))
        for x in list:
            print(text.format('\n', x['name'], x['lastname']))

    def register(self):
        email = input('\n Email: ')
        password = input('\n Password: ')
        name = input('\n Name: ')
        lastname = input('\n Lastname: ')
        os.system('cls')
        newUser = {"email": email, "password": password,
                   "name": name, "lastname": lastname}
        return newUser

    @notlogged
    def menu_login(self):
        if self.authorize():
            self.__authorized = True
        else:
            self.__authorized = False

    @notlogged
    def menu_register(self):
        newUser = self.register()
        if newUser != None:
            with open(filePath, 'r+') as file:
                self.__users = json.load(file)
                self.__users['users'].append(newUser)
                file.seek(0)
                json.dump(self.__users, file, indent=4)
            print(greenFont + '\n You have successfully registered.' + cEnd)

    @logged
    def menu_userslist(self):
        with open(filePath, 'r') as file:
            json_dict = json.load(file)
        self.display(json_dict['users'])
        input(orangeFont + '\n Press enter to back to menu..' + cEnd)
        os.system('cls')

    @logged
    def menu_logout(self):
        self.__authorized = False
        print(orangeFont + '\n You have been logged out.' + cEnd)

    @logged
    def menu_logged(self):
        print('\n Logged: ' + self.__name + ' ' + self.__lastname)
        print('\n 3 - Users List')
        print('\n 4 - Log out')
        print('\n 9 - Exit')

    @notlogged
    def menu_notlogged(self):
        print('\n 1 - Login')
        print('\n 2 - Register')
        print('\n 9 - Exit')

    def menu(self):

        while True:
            self.menu_logged()
            self.menu_notlogged()
            userInput = input('\n Enter a number from the menu: ')
            if userInput == '1':
                os.system('cls')
                self.menu_login()
            elif userInput == '2':
                os.system('cls')
                self.menu_register()
            elif userInput == '3':
                os.system('cls')
                self.menu_userslist()
            elif userInput == '4':
                os.system('cls')
                self.menu_logout()
            elif userInput == '9':
                exit()
            else:
                os.system('cls')


x = Network()
x.menu()
