#!/usr/bin/python3
"""
Initializes all modules required to run the app.
It turns our module into a package.
"""
from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()

from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
