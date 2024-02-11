#!/usr/bin/python3
"""
A module that creates a state with it attributes
"""
import uuid
from models import  base_model


class Place(base_model.BaseModel):
    """A blue print for creating a state object"""
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initializes the object"""
        super().__init__(*args, **kwargs)
