#!/usr/bin/python3
"""
Script that starts a Flask web application:
"""

from flask import Flask

app = Flask(__name__)

# Root URL i.e '/'
@app.route('/', strict_slashes=False)
def hello():
    """Returns string"""
    return "Hello HBNB!"


if __name__ == "__main__":
    # Flask development server
    app.run(host="0.0.0.0", port=5000)
