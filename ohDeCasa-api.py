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
    return 'status'

@app.route("/checkin", methods=['POST'])
#TODO deal with timezones
#TODO save in file
def checkin():
    raulOpen = True
    try:
        reqData = request.get_json()
        user = reqData['user']
    except KeyError:
        user = "Raul Seixas"
    currentTime = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    checkedUser = {'user': user, 'datetime': currentTime, 'open': raulOpen}
    checkedUsers[user] = checkedUser
    with open(usersFile, 'w') as file:
        json.dump(checkedUsers, file)
    return checkedUser



@app.route("/checkout")
def checkout():
    pass
