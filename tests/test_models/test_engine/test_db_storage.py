#!/usr/bin/env python3
"""
Test module for DBStorage class methods.
"""

import unittest
from unittest.mock import patch
from models.engine.db_storage import DBStorage
from models.user import User
from models.state import State


class TestDBStorageMethods(unittest.TestCase):
    def setUp(self):
        # Mock the database connection
        with patch('models.engine.db_storage.create_engine'):
            self.storage = DBStorage()
            self.storage.reload()

    def test_get_method(self):
        # Add test cases for the get method
        user = User()
        user_id = user.id
        self.storage.new(user)
        self.storage.save()
        retrieved_user = self.storage.get(User, user_id)
        self.assertEqual(retrieved_user, user)

        # Add more test cases as needed

    def test_count_method(self):
        # Add test cases for the count method
        user1 = User()
        state = State()
        user2 = User()
        self.storage.new(user1)
        self.storage.new(state)
        self.storage.new(user2)
        self.storage.save()
        user_count = self.storage.count(User)
        self.assertEqual(user_count, 2)

        # Add more test cases as needed


if __name__ == '__main__':
    unittest.main()
