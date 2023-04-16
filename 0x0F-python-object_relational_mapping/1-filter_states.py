#!/usr/bin/python3
"""
Lists all states with a name starting with N from the database hbtn_0e_0_usa.
Usage: ./1-filter_states.py <mysql username> \
                            <mysql password> \
                            <database name>
"""

import sys
import MySQLdb


if __name__ == "__main__":
    # Verify that the script is being used correctly
    if len(sys.argv) != 4:
        print("Usage: ./1-filter_states.py <mysql username> "
              "<mysql password> <database name>")
        sys.exit(1)

    # Connect to the MySQL server using the provided credentials
    try:
        db = MySQLdb.connect(user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3],
                             port=3306,
                             host="localhost")
    except MySQLdb.Error as e:
        print("Error connecting to the MySQL database: {}".format(e))
        sys.exit(1)

    # Create a cursor to execute queries
    cursor = db.cursor()

    # Select all the rows from the `states` table and order them by id
    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)

    # Fetch all the rows that match the query and print them if they start with 'N'
    for row in cursor.fetchall():
        if row[1][0] == "N":
            print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
