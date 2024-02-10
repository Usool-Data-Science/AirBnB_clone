#!/usr/bin/python3
"""
A module that creates a state with it attributes
"""
from models import  base_model


class Review(base_model.BaseModel):
    """A blue print for creating a state object"""
    place_id = ''
    user_id = ''
    text = ''

    def __init__(*args, **kwargs):
        """Initializes the object"""
        super.__init__(*args, **kwargs)
