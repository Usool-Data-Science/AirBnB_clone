#!/usr/bin/python3
"""
A module that creates a state with it attributes
"""
import uuid
from models import  base_model


class City(base_model.BaseModel):
    """A blue print for creating a state object"""
    name = ''
    state = uuid.uuid4()

    def __init__(self, *args, **kwargs):
        """Initializes the object"""
        super().__init__(*args, **kwargs)
