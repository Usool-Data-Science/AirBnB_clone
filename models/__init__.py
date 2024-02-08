#!/usr/bin/python3
"""
Initializes all modules required to run the app.
It turns our module into a package.
"""
from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()

