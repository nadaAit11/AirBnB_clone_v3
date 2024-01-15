#!/usr/bin/python3
"""
Initialize the BaseModel class with provided attributes or default values.
"""

import os
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage


# Create a FileStorage or DBStorage instance and
# reload data from the storage file.
if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()