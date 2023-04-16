#!/usr/bin/python3
"""
This script displays all values in the states table
where `name` matches the argument passed from the command line.
"""

import MySQLdb
import sys


def main():
    """
    Connects to the database and selects all rows that match the
    provided state name.
    """
    # Check for correct number of command-line arguments
    if len(sys.argv) != 5:
        print("Usage: {} username password database_name state_name"
              .format(sys.argv[0]))
        exit(1)

    # Connect to MySQL database using provided credentials
    try:
        db_connect = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8"
        )
    except Exception as e:
        print("Error connecting to database: {}".format(e))
        exit(1)

    # Create a cursor object to execute SQL queries
    db_cursor = db_connect.cursor()

    # Execute SQL query to select all rows where the name column matches
    # the provided argument, ordered by ID in ascending order
    query = "SELECT * FROM states WHERE name LIKE BINARY %(name)s ORDER BY id ASC"
    try:
        db_cursor.execute(query, {'name': sys.argv[4]})
    except Exception as e:
        print("Error executing query: {}".format(e))
        db_connect.close()
        exit(1)

    # Fetch all rows that match the query
    rows_selected = db_cursor.fetchall()

    # Print the selected rows
    for row in rows_selected:
        print(row)

    # Close the database connection
    db_connect.close()


if __name__ == "__main__":
    main()
