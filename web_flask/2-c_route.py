#!/usr/bin/python3
""" accepting variable in a url """

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """ serves Hello HBNB """
    return "Hello HBNB"


@app.route('/hbnb')
def hbnb():
    """ serves HBNB """
    return "HBNB"


@app.route('/c/<text>')
def hbnb_var(text):
    """ serves a text variable
    recieved from the user """
    return f'C {escape(text).replace("_", " ")}'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
