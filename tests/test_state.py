#!/usr/bin/python3
"""
A test case for user.py
"""
import unittest
from models.base_model import BaseModel
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    """A blue print for testing the user model"""
    def setUp(self):
        """Instantiate the user object"""
        self.user = State()

    def test_attributes(self):
        """Tests the presence of attributes"""
        self.assertTrue(hasattr(self.user, 'name'))

    def test_inheritance(self):
        """Test for the inheritance of the model"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_create_at(self):
        """Tests for the correctness of created_at attribute"""
        self.assertIsInstance(self.state.created_at, datetime)

    def test_updated_at(self):
        """Tests for the correctness of the updated_at attribute"""
        self.assertIsInstance(self.state.updated_at, datetime)

if __name__ == "__main__":
    unittest.main()
