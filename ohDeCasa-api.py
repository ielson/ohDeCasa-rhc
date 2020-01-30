from flask import Flask, request
import json
from datetime import datetime

app = Flask(__name__)

raulOpen = False
usersFile = "activeUsers.txt"
checkedUsers = {}

@app.route("/")
def index():
    return "RHC - ô de casa homepage"

@app.route("/status")
def status():
    usersAvailable = checkIfUsersAvailable()
    print(usersAvailable)
    return usersAvailable

@app.route("/checkin", methods=['POST'])
#TODO deal with timezones
def checkin():
    raulOpen = True
    checkIfUsersAvailable()
    try:
        reqData = request.get_json()
        user = reqData['user']
    except KeyError:
        user = "Raul Seixas"
    currentTime = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    checkedUser = {'user': user, 'datetime': currentTime, 'isThere': raulOpen}
    checkedUsers[user] = checkedUser
    checkedUsers['isOpen'] = raulOpen
    with open(usersFile, 'w') as file:
        json.dump(checkedUsers, file)
    return checkedUser


@app.route("/checkout")
def checkout():
    pass


def checkIfUsersAvailable():
    global checkedUsers
    try:
        if not checkedUsers:
            with open(usersFile, 'r') as file:
                checkedUsers = json.load(file)
        return checkedUsers
    except FileNotFoundError:
        return "No user ever checked in, please be the first sending a POST to /checkin"
