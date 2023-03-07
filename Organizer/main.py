import json
import os
import itertools
from os import path

redFont = '\x1b[38;2;255;0;0m'
greenFont = '\x1b[38;2;124;252;0m'
orangeFont = '\x1b[38;2;255;165;0m'
cEnd = '\x1b[0m'

filePath = 'C:/Users/Damian/Desktop/Python/Organizer/file.json'
listObj = []


def isFile():
    if path.isfile(filePath) is False:
        raise Exception('File not found.')


def startMenu():
    print('\n === Notebook v1.0 ===')
    print('\n 1. Show your notes.')
    print('\n 2. Add a note.')
    print('\n 3. Delete a note.')
    userInput = input('\n Enter 1 or 2: ')
    if userInput == "1":
        os.system('cls')
        showNotes()
    elif userInput == "2":
        os.system('cls')
        addNote()
    elif userInput == "3":
        os.system('cls')
        deleteNote()
    else:
        os.system('cls')
        startMenu()


def addNote():
    noteTitle = input('\n Enter note title: ')
    note = input('\n Enter the note: ')
    task = {
        "id": None,
        "title": noteTitle,
        "note": note
    }
    if noteTitle and note:
        editJson(task)
    else:
        os.system('cls')
        print(redFont + '\n Fill in all fields' + cEnd)
        addNote()


def deleteNote():
    print('\n Enter cancel to cancel deleting..')
    userInput = input('\n Enter note\'s id that you want to delete: ')
    if userInput == 'cancel':
        startMenu()
    else:
        if userInput.isdigit():
            userInput = int(userInput)
            with open(filePath, "r") as file:
                listObj = json.load(file)
                if userInput < 1 or userInput > len(listObj['tasks']):
                    os.system('cls')
                    print(redFont + '\n Note with given id does not exist..' + cEnd)
                    deleteNote()
                else:
                    for x in listObj['tasks']:
                        if x['id'] == userInput:
                            listObj['tasks'].pop(userInput-1)
                            with open(filePath, "w") as file:
                                json.dump(listObj, file, indent=4)
                            autoIndex()
                            os.system('cls')
                            print(greenFont + '\n Note deleted successfully.' + cEnd)
                            startMenu()
        else:
            os.system('cls')
            print(redFont + '\n You have to enter the id as a number..' + cEnd)
            deleteNote()


def editJson(task):
    isFile()

    with open(filePath, "r+") as file:
        listObj = json.load(file)
        task['id'] = len(listObj['tasks'])+1
        listObj['tasks'].append(task)
        file.seek(0)
        json.dump(listObj, file, indent=4)
    os.system('cls')
    print(greenFont + '\n Note added successfully.' + cEnd)
    startMenu()


def autoIndex():
    with open(filePath, "r+") as file:
        listObj = json.load(file)
        id_generator = itertools.count(1)
        for x in listObj['tasks']:
            x['id'] = next(id_generator)
        file.seek(0)
        json.dump(listObj, file, indent=4)


def isJsonEmpty():
    with open(filePath, "r") as file:
        listObj = json.load(file)
        if len(listObj['tasks']) == 0:
            print(orangeFont + '\n You have no notes. Write something first.' + cEnd)
            startMenu()


def showNotes():
    isFile()
    isJsonEmpty()
    autoIndex()

    print('\n === NOTES ===')
    with open(filePath, "r") as file:
        listObj = json.load(file)
        for x in listObj['tasks']:
            print('\n\n Id:', x['id'])
            print('\n Title:', x['title'])
            print('\n Note:', x['note'])

    input('\n\n Enter to return to menu: ')
    os.system('cls')
    startMenu()


startMenu()
