#!/usr/bin/python3
""" Place Module for HBNB project """

from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models


place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column(
        "place_id", String(60),
        ForeignKey("places.id"),
        primary_key=True,
        nullable=False),
    Column(
        "amenity_id", String(60),
        ForeignKey("amenities.id"),
        primary_key=True,
        nullable=False)
    )


class Place(BaseModel, Base):
    """Place class """

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship(
            "Review",
            cascade='all, delete, delete-orphan',
            backref="place")

        amenities = relationship(
            "Amenity",
            secondary=place_amenity,
            viewonly=False,
            back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """ Returns list of reviews.id """
            all_objects = models.storage.all()
            review_objects = []
            for value in all_objects.values():
                if isinstance(value, Review) and value.place_id == self.id:
                    review_objects.append(value)
            return review_objects

        @property
        def amenities(self):
            """ Return list of amenity ids """
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """Append amenity ids to the attribute """
            obj_cls_name = obj.to_dict().get("__class__", None)
            if obj_cls_name == "Amenity" and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
