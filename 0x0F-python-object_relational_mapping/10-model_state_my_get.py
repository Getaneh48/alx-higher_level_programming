#!/usr/bin/python3
"""
a script that prints the State object with the name passed as
argument from the database hbtn_0e_6_usa. also, prevents sql injection
attack
"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine, bindparam
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    search_key = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

# Filter State objects by name using bindparam to prevent SQL injection
    query = session.query(State).filter(State.name == bindparam('search_key'))

    # Set the value for the bind parameter (sanitize if needed)
    state = query.params(search_key=search_key).first()
    if state:
        print(state.id)
    else:
        print("Not Found")
    session.close()
