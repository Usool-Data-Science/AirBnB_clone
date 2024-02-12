#!/usr/bin/python3
"""A test case for file_storage.py"""
import unittest
from unittest.mock import patch, mock_open
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    """A blue print for testing file_storage.py methods"""
    def setUp(self):
        """Instantiate FileStorage() before any test"""
        self.storage = FileStorage()

    def test_all(self):
        """Tests the correctness of the all() method"""
        self.assertEqual(self.storage.all(), self.storage._FileStorage__objects)

    def test_new(self):
        """Tests the correctness of the new() method"""
        obj = BaseModel()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.storage.new(obj)
        self.assertIn(key, self.storage._FileStorage__objects)

    @patch('builtins.open', new_callable=mock_open)
    def test_save(self, mock_open):
        """Tests the correctness of the save() method"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        mock_open.assert_called_once_with(self.storage._FileStorage__file_path, 'w', encoding='UTF-8')
        mock_open().write.assert_called_once_with(json.dumps({f'{obj.__class__.__name__}.{obj.id}': obj.to_dict()}))

    def test_destroy(self):
        """Tests the correctness of destroy() method"""
        obj = BaseModel()
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.storage.new(obj)
        self.storage.destroy(key)
        self.assertNotIn(key, self.storage._FileStorage__objects)


if __name__ = "__main__":
    unittest.main()
