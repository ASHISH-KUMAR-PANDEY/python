import string
import random
from random import *

users = {}
status = ""

def displayMenu():
    status = input("Are you registered user? y/n? Press q to quit")
    if status == "y":
        oldUser()
    elif status == "n":
        newUser()

def newUser():
    createLogin = input("Create login name: ")

    if createLogin in users:
        print("\nLogin name already exist!\n")
    else:
        characters = string.ascii_letters + string.punctuation  + string.digits
        password =  "".join(choice(characters) for x in range(randint(8, 16)))
        print ("your password is: ", password)
        print ("USER CREATED")


def oldUser():
    login = input("Enter login name: ")
    passw = input("Enter password: ")

    if login in users and users[login] == passw:
        print("\nLogin successful!\n")
    else:
        print("\nUser doesn't exist or wrong password!\n")

while status != "q":
    displayMenu()
