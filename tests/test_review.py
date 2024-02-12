#!/usr/bin/python3
"""
A test case for user.py
"""
import unittest
from models.base_model import BaseModel
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    """A blue print for testing the user model"""
    def setUp(self):
        """Instantiate the user object"""
        self.user = Review()

    def test_attributes(self):
        """Tests the presence of attributes"""
        self.assertTrue(hasattr(self.user, 'place_id'))
        self.assertTrue(hasattr(self.user, 'user_id'))
        self.assertTrue(hasattr(self.user, 'passwor'))
        self.assertTrue(hasattr(self.user, 'text'))

    def test_inheritance(self):
        """Test for the inheritance of the model"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_create_at(self):
        """Tests for the correctness of created_at attribute"""
        self.assertIsInstance(self.review.created_at, datetime)

    def test_updated_at(self):
        """Tests for the correctness of the updated_at attribute"""
        self.assertIsInstance(self.review.updated_at, datetime)

if __name__ == "__main__":
    unittest.main()
