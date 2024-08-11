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

# Initialize the Flask application
app = Flask(__name__)

# Optional Jinja template settings for whitespace control
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True

@app.teardown_appcontext
def close_db(error):
    """ Closes the SQLAlchemy session after each request """
    storage.close()

@app.route('/3-hbnb/', strict_slashes=False)
def hbnb():
    """ Renders the HBNB page with sorted data for version 3 """
    # Fetch and sort all state objects by their names
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    # Compile a list of states with their cities, sorted by city name
    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    # Fetch and sort all amenities by name
    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    # Fetch and sort all places by name
    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    # Create a unique cache identifier
    cache_id = str(uuid4())

    # Render the HTML page with sorted data and unique cache ID
    return render_template('3-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places,
                           cache_id=cache_id)

if __name__ == "__main__":
    """ Launches the Flask development server """
    app.run(host='0.0.0.0', port=5000)
