#!/usr/bin/python3
"""A simple use of sqlalchmey
"""
import sys
from requests import Session
from sqlalchemy import create_engine
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    params = sys.argv
    engin = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                          format(params[1], params[2], params[3]),
                          pool_pre_ping=True)

    with Session(engin) as session:
        query = session.query(City)
        content = query.all()

        for city, state in content:
            print("{}: {} -> {}".format(city.id, city.name, city.state.name))