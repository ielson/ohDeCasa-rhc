from flask import Flask, request
import json
from datetime import datetime

app = Flask(__name__)

usersFile = "activeUsers.txt"
checkedUsers = {}

@app.route("/")
def index():
    return "RHC - Ô de casa homepage"

@app.route("/status")
def status():
    availableUsers = checkIfUsersAvailable()
    return availableUsers

@app.route("/checkin", methods=['POST'])
#TODO deal with timezones
def checkin():
    checkIfUsersAvailable()
    try:
        reqData = request.get_json()
        user = reqData['user']
    except KeyError:
        user = "Raul Seixas"
    currentTime = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    checkedUser = {'user': user, 'datetime': currentTime, 'isThere': True}
    checkedUsers[user] = checkedUser
    with open(usersFile, 'w') as file:
        json.dump(checkedUsers, file)
    return checkedUser


@app.route("/checkout", methods=['POST'])
def checkout():
    global checkedUsers
    checkIfUsersAvailable()
    try:
        reqData = request.get_json()
        user = reqData['user']
        del checkedUsers[user]
        with open(usersFile, 'w') as file:
            json.dump(checkedUsers, file)
        currentTime = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        checkedUser = {'user': user, 'datetime': currentTime, 'isThere': False}
        return checkedUser
    except KeyError:
        return "User was not checked-in, could not check-out"


def checkIfUsersAvailable():
    global checkedUsers
    try:
        if not checkedUsers:
            with open(usersFile, 'r') as file:
                checkedUsers = json.load(file)
        print(len(checkedUsers))
        if len(checkedUsers) > 1:
            raulOpen = True
            print("raul open")
        else:
            raulOpen = False
            print('raul closed ')
        checkedUsers['isOpen'] = raulOpen
        return checkedUsers
    except FileNotFoundError:
        return "No user ever checked in, please be the first sending a POST to /checkin"
