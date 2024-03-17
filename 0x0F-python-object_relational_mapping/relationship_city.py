#!/usr/bin/python3
"""
A simple use of sqlalchmey
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class City(Base):
    """Represents a city for a MySQL database.

        Attributes:
            id (str): The city's id.
            name (sqlalchemy.Integer): The city's name.
            state_id (sqlalchemy.String): The city's state id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
    name = Column(String(128), nullable=False)