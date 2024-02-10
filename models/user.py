#!/usr/bin/python3
"""
A module for creating User object.
"""
import uuid
from models import base_model


class User(base_model.BaseModel):
    """A blue print for creating a User object"""
    id = uuid.uuid4()
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """Initializes the User class"""
        super().__init__(*args, **kwargs)
