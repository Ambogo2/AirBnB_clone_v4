#!/usr/bin/python3
""" Initializes and launches a Flask Web Application """
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template
from uuid import uuid4

# Create a Flask application instance
app = Flask(__name__)

# Uncomment these lines to enable trimming of whitespace in Jinja templates
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True

@app.teardown_appcontext
def close_db(error):
    """ Closes the SQLAlchemy session at the end of each request """
    storage.close()

@app.route('/0-hbnb/', strict_slashes=False)
def hbnb():
    """ Renders the main page of the HBNB application """
    # Retrieve and sort states
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    # Collect state and their cities, sorted by name
    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    # Retrieve and sort amenities
    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    # Retrieve and sort places
    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    # Generate a unique cache identifier
    cache_id = str(uuid4())

    # Render the HTML template with the gathered data
    return render_template('0-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places,
                           cache_id=cache_id)

if __name__ == "__main__":
    """ Starts the Flask development server """
    app.run(host='0.0.0.0', port=5000)
