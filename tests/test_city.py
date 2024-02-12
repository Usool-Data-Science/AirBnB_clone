#!/usr/bin/python3
"""
A test case for user.py
"""
import unittest
from models.base_model import BaseModel
from models.city import City
from datetime import datetime


class TestUser(unittest.TestCase):
    """A blue print for testing the user model"""
    def setUp(self):
        """Instantiate the user object"""
        self.user = City()

    def test_attributes(self):
        """Tests the presence of attributes"""
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertTrue(hasattr(self.city, 'state'))

    def test_inheritance(self):
        """Test for the inheritance of the model"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_create_at(self):
        """Tests for the correctness of created_at attribute"""
        self.assertIsInstance(self.city.created_at, datetime)

    def test_updated_at(self):
        """Tests for the correctness of the updated_at attribute"""
        self.assertIsInstance(self.city.updated_at, datetime)

if __name__ == "__main__":
    unittest.main()
