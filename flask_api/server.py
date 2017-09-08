import os
import datetime
import plaid
import plaid_config
import requests
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask_api import FlaskAPI

app = FlaskAPI(__name__)

PLAID_CLIENT_ID = plaid_config.CLIENT_ID
PLAID_SECRET = plaid_config.SECRET
PLAID_PUBLIC_KEY = plaid_config.PUBLIC_KEY
PLAID_ENV = plaid_config.ENV


@app.route("/api")
def index():
    r = requests.get("https://www.reddit.com/r/spaceporn/.json?")
    print "The server is running. You'd better catch it!"
    return r.json()

if __name__ == "__main__":
    app.run()
