import os
import datetime
import plaid
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

app = Flask(__name__)


PLAID_CLIENT_ID = '59ab3519bdc6a43c31e518a3'
PLAID_SECRET = '342e5fcbe9ea7dbc71097d4f54c568'
PLAID_PUBLIC_KEY = '99d40644c2dfd609a4e9378c9fdd47'
PLAID_ENV ='sandbox'

@app.route("/")
def index():
    print "The server is running. You'd better catch it!"
    return render_template('index.ejs')
@app.route("/page")
def page():
    return render_template('page.ejs')








if __name__ == "__main__":
    app.run()
