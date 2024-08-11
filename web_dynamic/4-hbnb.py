#!/usr/bin/python3
""" Initializes and runs a Flask Web Application for HBNB """
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template
import uuid

# Create an instance of the Flask application
app = Flask(__name__)

# Optional configuration for Jinja template whitespace handling
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True

@app.teardown_appcontext
def close_db(error):
    """ Closes the current SQLAlchemy session after each request """
    storage.close()

@app.route('/4-hbnb', strict_slashes=False)
def hbnb():
    """ Renders the HBNB page with data for version 4 """
    # Retrieve and sort state objects by name
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    # Prepare a list of states with their sorted cities
    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    # Retrieve and sort amenities by name
    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)
    # Uncomment the following lines to print amenity names
    # for amenity in amenities:
    #     print(amenity.name)

    # Retrieve and sort places by name
    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    # Generate a unique UUID for cache management
    return render_template('4-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places,
                           cache_id=uuid.uuid4())

if __name__ == "__main__":
    """ Starts the Flask development server """
    app.run(host='0.0.0.0', port=5000)
