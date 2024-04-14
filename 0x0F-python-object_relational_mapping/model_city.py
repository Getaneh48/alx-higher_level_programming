#!/usr/bin/python3
"""
a Python file similar to model_state.py named model_city.py that contains
the class definition of a City
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData, ForeignKey

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class City(Base):
    """
    a city model
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
