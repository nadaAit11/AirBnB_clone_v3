#!/usr/bin/python3
"""
Defines the User class.
"""
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.place import Place


class User(BaseModel, Base):
    """
    Represent a User.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store Users.
        email (Column): The email of the user.
        password (Column): The password of the user.
        first_name (Column): The user's first name.
        last_name (Column): The user's last name.
        places (relationship): The User-Place relationship.
    """
    # Represents the table name, users
    __tablename__ = 'users'

    # Represents a column containing a string (128 characters)
    # and can’t be null
    email = Column(String(128), nullable=False)

    # Represents a column containing a string (128 characters)
    # and can’t be null
    password = Column(String(128), nullable=False)

    # Represents a column containing a string (128 characters) and can be null
    first_name = Column(String(128), nullable=True)

    # Represents a column containing a string (128 characters) and can be null
    last_name = Column(String(128), nullable=True)

    # Represents a relationship with the class Place
    places = relationship("Place", backref="user", cascade="all, delete")