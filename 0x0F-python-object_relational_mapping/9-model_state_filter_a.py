#!/usr/bin/python3
"""
a script that lists all State objects that contain the letter a from the
database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    filter_s = State.name.like("%a%")
    result = session.query(State).filter(filter_s).order_by(State.id)
    for state in result:
        print(f"{state.id}: {state.name}")
