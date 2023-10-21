#!/usr/bin/python3
"""
Script that creates Flask web application with followig route:

Route:
    /cities_by_states: display a HTML page: (inside the tag BODY)
    H1 tag: “States”
    UL tag: with the list of all State objects present in DBStorage
            sorted by name (A->Z) tip
    LI tag: description of one State: <state.id>: <B><state.name></B> +
            UL tag: with the list of City objects linked to the State
            sorted by name (A->Z)
    LI tag: description of one City: <city.id>: <B><city.name></B>
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Clean up tasks"""
    storage.close()


# Route: '/cities_by_states'
@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Displays an Html page with cites by states"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
