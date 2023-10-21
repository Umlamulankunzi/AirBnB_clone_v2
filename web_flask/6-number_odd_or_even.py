#!/usr/bin/python3
"""
Script that starts a Flask web application:
"""
from flask import Flask, render_template

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


# Route: '/number/<n>'
@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Returns astring"""
    return "{} is a number".format(n)


# Route: '/number_template/<n>'
@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Renders an Html page if n is int"""
    return render_template("5-number.html", n=n)

# Route: '/number_odd_or_even/<n>'
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n=None):
    """Display an HTML page if n is int.

    States if number is even or odd in html page"""
    if isinstance(n, int):
        n_odd_or_even = "odd" if n % 2 != 0 else "even"
        return render_template(
            "6-number_odd_or_even.html", n=n, n_odd_or_even=n_odd_or_even)


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
