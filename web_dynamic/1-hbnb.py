#!/usr/bin/python3
""" Initializes and runs a Flask Web Application for HBNB """
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template
from uuid import uuid4

# Create the Flask application instance
app = Flask(__name__)

# Optional settings for Jinja template whitespace control
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True

@app.teardown_appcontext
def close_db(error):
    """ Cleans up the SQLAlchemy session after each request """
    storage.close()

@app.route('/1-hbnb/', strict_slashes=False)
def hbnb():
    """ Displays the main HBNB page with sorted data """
    # Fetch and sort all states by name
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    # Prepare a list of states with their cities, both sorted by name
    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    # Fetch and sort all amenities by name
    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    # Fetch and sort all places by name
    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    # Create a unique cache identifier for the page
    cache_id = str(uuid4())

    # Render the HTML page with the sorted data and cache identifier
    return render_template('1-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places,
                           cache_id=cache_id)

if __name__ == "__main__":
    """ Launches the Flask application on the specified host and port """
    app.run(host='0.0.0.0', port=5000)
