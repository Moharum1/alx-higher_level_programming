#!/usr/bin/python3
"""A simple use of sqlalchmey
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_city import City
from model_state import State
import sys

if __name__ == "__main__":
    params = sys.argv
    engin = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                          format(params[1], params[2], params[3]),
                          pool_pre_ping=True)

    with Session(engin) as session:
        query = session.query(City, State)\
                        .filter(City.state_id == State.id)\
                        .order_by(City.id)
        content = query.all()

        for city, state in content:
            print("{}: ({}) {}".format(state.name, city.id, city.name))
