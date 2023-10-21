#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    if os.getenv("HBNB_TYPE_STORAGE") == "file":
        name = ""
    else:
        name = Column(String(128), nullable=False)
        cities = relationship(
            'City', cascade='all, delete-orphan', backref="state")

    @property
    def cities(self):
        """Returns the list of City instances with state_id"""

        city_objects = []

        for city in models.storage.all(City).values():
            if city.state_id == self.id:
                city_objects.append(city)
        return city_objects
