#!/usr/bin/python3
""" Launches a Flask Web Application for HBNB """
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template
from uuid import uuid4

# Initialize the Flask application instance
app = Flask(__name__)

# Optional Jinja configuration for trimming and left-stripping blocks
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True

@app.teardown_appcontext
def close_db(error):
    """ Clean up the SQLAlchemy session after each request """
    storage.close()

@app.route('/2-hbnb/', strict_slashes=False)
def hbnb():
    """ Renders the HBNB page with data sorted by name """
    # Retrieve and sort all states by name
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    # Create a list of states with their cities, sorted by city name
    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    # Retrieve and sort amenities by name
    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    # Retrieve and sort places by name
    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    # Generate a unique identifier for cache management
    cache_id = str(uuid4())

    # Render the HTML template with sorted data and cache ID
    return render_template('2-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places,
                           cache_id=cache_id)

if __name__ == "__main__":
    """ Runs the Flask app on the specified network address and port """
    app.run(host='0.0.0.0', port=5000)
