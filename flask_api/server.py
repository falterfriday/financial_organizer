import os
import datetime
import plaid
from plaid_config import CLIENT_ID, ENV, PUBLIC_KEY, SECRET
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

app = Flask(__name__)

PLAID_CLIENT_ID = plaid_config.CLIENT_ID
PLAID_SECRET = plaid_config.SECRET
PLAID_PUBLIC_KEY = plaid_config.PUBLIC_KEY
PLAID_ENV = plaid_config.ENV


@app.route("/api")
def index():
    print "The server is running. You'd better catch it!"

if __name__ == "__main__":
    app.run()
