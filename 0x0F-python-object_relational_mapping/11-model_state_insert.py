#!/usr/bin/python3
"""
This script adds a new State object to the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Connect to the database using provided credentials
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_url)
    
    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Create a new State object with name "Louisiana" and add it to the database
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Print the id of the newly added State object and close the session
    print('{0}'.format(new_state.id))
    session.close()
