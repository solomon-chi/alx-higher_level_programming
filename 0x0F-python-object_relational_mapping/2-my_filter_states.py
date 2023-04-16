#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states
where `name` matches the argument from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    """
    Access to the database and get the states from the database.
    """

    # Check for correct number of command-line arguments
    if len(argv) != 5:
        print("Usage: {} username password database_name state_name"
              .format(argv[0]))
        exit(1)

    # Connect to MySQL database using provided credentials
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset="utf8"
        )
    except Exception as e:
        print("Error connecting to database: {}".format(e))
        exit(1)

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute SQL query to select all rows where the name column matches
    # the provided argument, ordered by ID in ascending order
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    try:
        cursor.execute(query, (argv[4],))
    except Exception as e:
        print("Error executing query: {}".format(e))
        db.close()
        exit(1)

    # Fetch all rows that match the query
    rows_selected = cursor.fetchall()

    # Print the selected rows
    for row in rows_selected:
        print(row)

    # Close the database connection
    db.close()
#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states
where `name` matches the argument from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    """
    Access to the database and get the states from the database.
    """

    # Check for correct number of command-line arguments
    if len(argv) != 5:
        print("Usage: {} username password database_name state_name"
              .format(argv[0]))
        exit(1)

    # Connect to MySQL database using provided credentials
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset="utf8"
        )
    except Exception as e:
        print("Error connecting to database: {}".format(e))
        exit(1)

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute SQL query to select all rows where the name column matches
    # the provided argument, ordered by ID in ascending order
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    try:
        cursor.execute(query, (argv[4],))
    except Exception as e:
        print("Error executing query: {}".format(e))
        db.close()
        exit(1)

    # Fetch all rows that match the query
    rows_selected = cursor.fetchall()

    # Print the selected rows
    for row in rows_selected:
        print(row)

   # Close the database connection
    db.close()
