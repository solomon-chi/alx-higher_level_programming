#!/usr/bin/python3
"""
This script takes in the name of a state as an argument
and lists all cities of that state, using the database `hbtn_0e_4_usa`.
"""

# Import necessary modules
import MySQLdb as db
from sys import argv

if __name__ == "__main__":
    # Check if the script is being run as the main program

    # Connect to the database using command-line arguments
    db_connect = db.connect(
        host="localhost", port=3306,
        user=argv[1], passwd=argv[2], db=argv[3]
    )

    # Create a cursor object to interact with the database
    with db_connect.cursor() as cursor:
        # Execute a SELECT query to retrieve cities of the specified state
        cursor.execute("""
            SELECT
                cities.id, cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %(state_name)s
            ORDER BY
                cities.id ASC
        """, {
            'state_name': argv[4]
        })

        # Fetch all the rows of the query result
        rows_selected = cursor.fetchall()

    # Print the names of the cities
    if rows_selected is not None:
        print(", ".join([row[1] for row in rows_selected]))
