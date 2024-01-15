#!/usr/bin/python3
"""
This module defines the State class, which represents a state in the
HBNB project.
It inherits from the BaseModel and Base classes and provides
attributes for state name.
"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """
    Represents a state in the system.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store States.
        name (Column): The name of the State.
        cities (relationship): The State-City relationship.
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    # For DBStorage
    cities = relationship("City", backref="state", cascade="all, delete")

    # For FileStorage
    @property
    def cities(self):
        """
        Returns the list of City instances with state_id
        equals to the current State.id
        """
        all_cities = models.storage.all(City).values()
        return [city for city in all_cities if city.state_id == self.id]