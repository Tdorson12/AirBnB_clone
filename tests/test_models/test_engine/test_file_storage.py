#!/usr/bin/python3
"""
Unittest for FileStorage class
"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class"""

    def setUp(self):
        """Set up for the test"""
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up after the test"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_instance_creation(self):
        """Test the creation of a FileStorage instance"""
        self.assertIsInstance(self.storage, FileStorage)

    def test_all_method(self):
        """Test the all method of FileStorage class"""
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertEqual(all_objects, {})

    def test_new_method(self):
        """Test the new method of FileStorage class"""
        my_model = BaseModel()
        self.storage.new(my_model)
        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 1)
        self.assertIn("BaseModel." + my_model.id, all_objects)

    def test_save_method(self):
        """Test the save method of FileStorage class"""
        my_model = BaseModel()
        self.storage.new(my_model)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", 'r', encoding='utf-8') as file:
            saved_content = file.read()
            self.assertIn("BaseModel." + my_model.id, saved_content)

    def test_reload_method(self):
        """Test the reload method of FileStorage class"""
        my_model = BaseModel()
        self.storage.new(my_model)
        self.storage.save()
        self.storage.reload()
        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 1)
        self.assertIn("BaseModel." + my_model.id, all_objects)

    def test_reload_nonexistent_file(self):
        """Test the reload method when the file doesn't exist"""
        self.storage.reload()
        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 0)

    def test_reload_multiple_classes(self):
        """Test the reload method with multiple classes"""
        user = User()
        user_id = user.id
        self.storage.new(user)
        self.storage.save()

        base_model = BaseModel()
        base_model_id = base_model.id
        self.storage.new(base_model)
        self.storage.save()

        self.storage.reload()

        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 2)
        self.assertIn("User." + user_id, all_objects)
        self.assertIn("BaseModel." + base_model_id, all_objects)


if __name__ == '__main__':
    unittest.main()
