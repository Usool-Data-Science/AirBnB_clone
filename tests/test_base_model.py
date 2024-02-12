#!/usr/bin/python3
"""
Test cases for base_model.py
"""
import unittest
from unittest.mock import  MagicMock
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    A blue print for the BaseModel test cases.
    """

    def SetUp(self):
        """Create a BaseModel instance"""
        self.base_model = BaseModel()

    def test_init_without_kwargs(self):
        """
        Test the resutl of init model
        if with a new model
        """
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_init_with_kwargs(self):
        """Test for initialization with **kwargs"""
        test_id = "test_id"
        created_at = datetime(2024, 1, 1, 0, 0, 0)
        updated_at = datetime(2025, 1, 1, 0, 0, 0)
        kwargs = {
            'id': test_id,
            'created_at': created_at.isoformat(),
            'update_at': updated_at.isoformat(),
            'extra_attr': 'extra_value'
            }
        base_model = BaseModel(**kwargs)
        self.assertEqual(base_model.id, test_id)
        self.assertEqual(base_model.created_at, created_at)
        self.assertEqual(base_model.updated_at, updated_at)
        self.assertEqual(base_model.extra_attr, 'extra_value')

    def test_save(self):
        """Test the correctness of the save method"""
        self.base_model.update_at = datetime(2025, 1, 1, 0, 0, 0)
        models = MagicMock()
        models.storage = MagicMock()
        self.base_model.save()
        self.assertEqual(self. base_model.updated_at, datetime.now())
        models.storage.save.assert_called_once()

    def test_to_dict(self):
        """Test for the correctness of the to_dict method"""
        self.base_model.id = 'test_id'
        self.base_model.created_at = datetime(2024, 1, 1, 0, 0, 0)
        self.base_model.update_at = datetime(2025, 1, 1, 0, 0, 0)
        expected_dict = {
            '__class__': 'BaseModel',
            'id': 'test_id',
            'created_at': '2024, 1, 1, 0, 0, 0',
            'update_at': '2025, 1, 1, 0, 0, 0'
        }
        self.assertEqual(self.base_model.to_dict(), expected_dict)


if __name__ == '__main__':
    unittest.main()
