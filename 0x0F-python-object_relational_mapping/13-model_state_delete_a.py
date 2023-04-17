#!/usr/bin/python3
"""
This script deletes all State objects with a name containing
the letter 'a' from the database 'hbtn_0e_6_usa'.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    # Connect to the database
    db_url = "mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Delete all State objects containing 'a' in their name
    for state in session.query(State):
        if "a" in state.name:
            session.delete(state)
    session.commit()
