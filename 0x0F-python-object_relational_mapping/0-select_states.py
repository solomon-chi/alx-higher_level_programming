#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa."""
import sys
import MySQLdb


if __name__ == "__main__":
    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306,
                         charset="utf8")

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query to select all states
    cursor.execute("SELECT * FROM states")

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and database connections
    cursor.close()
    db.close()
