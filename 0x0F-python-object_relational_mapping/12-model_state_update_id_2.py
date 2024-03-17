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
        query = session.query(State)
        content = query.all()

        for item in content:
            if item.id == 2:
                item.name = "New Mexico"
                session.commit()
