import json
import os
import itertools
from os import path

redFont = '\x1b[38;2;255;0;0m'
greenFont = '\x1b[38;2;124;252;0m'
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


def showNotes():
    isFile()

    with open(filePath, "r+") as file:
        listObj = json.load(file)
        id_generator = itertools.count(1)
        print('\n === NOTES ===')
        for x in listObj['tasks']:
            x['id'] = next(id_generator)
            print('\n\n Id:', x['id'])
            print('\n Title:', x['title'])
            print('\n Note:', x['note'])
        file.seek(0)
        json.dump(listObj, file, indent=4)
    input('\n\n Enter to return to menu: ')
    os.system('cls')
    startMenu()


startMenu()
