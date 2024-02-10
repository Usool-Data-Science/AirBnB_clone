#!/usr/bin/python3
"""
A module that creates a state with it attributes
"""
from models import  base_model


class State(base_model.BaseModel):
    """A blue print for creating a state object"""
    name = ''

    def __init__(*args, **kwargs):
        """Initializes the object"""
        super.__init__(*args, **kwargs)
