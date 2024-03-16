#!/usr/bin/python3
"""A simple use of sqlalchmey
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import State
import sys

if __name__ == "__main__":
    params = sys.argv
    engin = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                          format(params[1], params[2], params[3]),
                          pool_pre_ping=True)

    with Session(engin) as session:
        state = State(name="Louisiana")
        query = session.add(state)
        session.commit()

        print(state.id)
