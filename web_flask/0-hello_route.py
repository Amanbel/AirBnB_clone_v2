#!/usr/bin/python3
""" using flask to run a
local server to serve text """

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_hbtn():
    """ function that serves
    the text Hello HBNB! """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
