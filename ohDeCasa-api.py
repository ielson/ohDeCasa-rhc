from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def index():
    return "RHC - ô de casa homepage"

@app.route("/status")
def status():
    pass

@app.route("/checkin")
def checkin():
    pass

@app.route("/checkout")
def checkout():
    pass
