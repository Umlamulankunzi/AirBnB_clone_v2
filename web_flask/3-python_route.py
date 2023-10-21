#!/usr/bin/python3
"""
Script that starts a Flask web application:
"""

from flask import Flask

app = Flask(__name__)


# Route: root '/'
@app.route('/', strict_slashes=False)
def hello():
    """Returns a string"""
    return "Hello HBNB!"


# Route: '/hbnb'
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns a given string"""
    return "HBNB"


# Route: '/c/<text>'
@app.route("/c/<text>", strict_slashes=False)
def cText(text):
    """Display C followed by value of the text parameter"""
    parsed_text = "C {}".format(text.replace("_", " "))
    return parsed_text


# Route '/python'
# Route '/python/<text>
@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonText(text="is cool"):
    """Display Python followed by value of the text variable"""
    parsed_text = "Python {}".format(text.replace("_", " "))
    return parsed_text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
