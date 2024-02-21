#!/usr/bin/python3
"""
A test case for user.py
"""
import unittest
from models.base_model import BaseModel
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    """A blue print for testing the user model"""
    def setUp(self):
        """Instantiate the user object"""
        self.user = User()

    def test_attributes(self):
        """Tests the presence of attributes"""
        self.assertTrue(hasattr(self.user, 'id'))
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'passwor'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_inheritance(self):
        """Test for the inheritance of the model"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_create_at(self):
        """Tests for the correctness of created_at attribute"""
        self.assertIsInstance(self.user.created_at, datetime)

    def test_updated_at(self):
        """Tests for the correctness of the updated_at attribute"""
        self.assertIsInstance(self.user.updated_at, datetime)

if __name__ == "__main__":
    unittest.main()
