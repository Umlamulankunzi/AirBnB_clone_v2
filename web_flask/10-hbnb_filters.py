#!/usr/bin/python3
"""
Script that creates Flask web application with followig routes:

Routes:
    /hbnb_filters: HBnB HTML filters page.
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


# Route: '/hbnb_filters'
@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Display HBnB filters HTML page."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template(
        "10-hbnb_filters.html", states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exception):
    """Performs Cleanup"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
