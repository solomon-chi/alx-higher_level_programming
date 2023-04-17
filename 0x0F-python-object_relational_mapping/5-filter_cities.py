#!/usr/bin/python3
"""
This script takes the name of a state as an argument and lists all cities of that
state, using the database `hbtn_0e_4_usa`.
"""

# Import necessary modules
import MySQLdb as db
from sys import argv


if __name__ == "__main__":
    # Check if the script is being run as the main program

    # Connect to the MySQL database using command-line arguments
    db_connect = db.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    # Create a cursor object to execute SQL queries
    with db_connect.cursor() as db_cursor:
        # Execute an SQL query to select all cities in the specified state
        db_cursor.execute("""
            SELECT cities.id, cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name LIKE BINARY %(state_name)s
            ORDER BY cities.id ASC
        """, {
            'state_name': argv[4]
        })

        # Fetch all rows selected by the query
        rows_selected = db_cursor.fetchall()

    # Check if any rows were selected
    if rows_selected is not None:
        # Print the names of all cities in the specified state
        # Join city names with commas
        city_names = [row[1] for row in rows_selected]
        print(", ".join(city_names))

