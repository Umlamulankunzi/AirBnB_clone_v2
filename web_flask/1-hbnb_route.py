#!/usr/bin/python3
"""
Script that starts a Flask web application:
"""

from flask import Flask

app = Flask(__name__)


# Define root
@app.route('/', strict_slashes=False)
def hello():
    """Returns a string"""
    return ("Hello HBNB!")


# Define path /hbnb
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns a string"""
    return ("HBNB")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
