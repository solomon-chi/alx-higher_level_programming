#!/usr/bin/python3
"""
This script defines a State class and
a Base class to work with MySQLAlchemy ORM.
"""

# Import necessary modules
import sys
from model_state import Base, State
from sqlalchemy import create_engine


if __name__ == "__main__":
    # Check if the script is being run as the main program

    # Create an engine object to connect to a MySQL database using command-line arguments
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Create tables in the database using the metadata of the Base class
    Base.metadata.create_all(engine)
