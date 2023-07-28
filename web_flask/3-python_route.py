#!/usr/bin/python3
""" serving pages that accept variables """

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """ serves Hello HBNB """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """ serves HBNB """
    return "HBNB"


@app.route('/c/<text>')
def hbnb_c(text):
    """ serves C <text> text
    implying a variable """
    return f'C {escape(text).replace("_", " ")}'


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def hbnb_python(text):
    """ serves Python is cool as a default but it can
    accept a variable in place of 'is cool' """
    return f'Python {escape(text).replace("_", " ")}'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
