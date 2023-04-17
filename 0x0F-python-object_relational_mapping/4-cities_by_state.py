#!/usr/bin/python3
"""
This script lists all cities from
the database `hbtn_0e_4_usa`.
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    """
    Access the database and get the cities
    from the database.
    """

    # Connect to the MySQL database using the provided credentials
    db_connect = db.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    # Execute SQL query to select all cities from the cities table
    # and join with the states table to get the corresponding state names
    with db_connect.cursor() as db_cursor:
        db_cursor.execute(
            "SELECT cities.id, cities.name, states.name "
            "FROM cities JOIN states ON cities.state_id = states.id "
            "ORDER BY cities.id ASC"
        )
        rows_selected = db_cursor.fetchall()

    # Print the selected rows, if any
    if rows_selected:
        for row in rows_selected:
            print(row)

    # Close the database connection
    db_connect.close()
