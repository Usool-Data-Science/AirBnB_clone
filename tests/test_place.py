#!/usr/bin/python3
"""
A test case for user.py
"""
import unittest
from models.base_model import BaseModel
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):
    """A blue print for testing the user model"""
    def setUp(self):
        """Instantiate the user object"""
        self.user = Place()

    def test_attributes(self):
        """Tests the presence of attributes"""
        attributes = ['city_id', 'user_id', 'name', 'description',
                      'number_rooms', 'number_bathrooms', 'max_guest',
                      'price_by_night', 'latitude', 'longitude', 'amenity_ids']
        for attr in attributes:
            self.asserTrue(hasattr(self.place, attr))

    def test_inheritance(self):
        """Test for the inheritance of the model"""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_create_at(self):
        """Tests for the correctness of created_at attribute"""
        self.assertIsInstance(self.place.created_at, datetime)

    def test_updated_at(self):
        """Tests for the correctness of the updated_at attribute"""
        self.assertIsInstance(self.place.updated_at, datetime)

if __name__ == "__main__":
    unittest.main()
