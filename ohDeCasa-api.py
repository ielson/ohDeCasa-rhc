from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

open = False

@app.route("/")
def index():
    return "RHC - ô de casa homepage"

@app.route("/status")
def status():
    return 'status'

@app.route("/checkin", methods=['POST'])
#TODO deal with timezones
def checkin():
    open = True
    try:
        reqData = request.get_json()
        print(reqData)
        print('depois')
        user = reqData['user']
    except KeyError:
        user = "Raul Seixas"
    checkedUser = {'user': user, 'datetime':datetime.now(), 'open': open}
    return checkedUser



@app.route("/checkout")
def checkout():
    pass
