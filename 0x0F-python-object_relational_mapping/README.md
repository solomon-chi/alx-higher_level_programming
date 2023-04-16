Title: Python - Object-relational mapping

Introduction:
In this project, the focus is on the concept of object-relational mapping used in database scripting. The project aims to provide the basic understanding of using libraries such as MySQLdb and SQLAlchemy to perform create, read, update and delete operations on MySQL databases.

Content:
The project consists of 15 tasks, which are briefly described below:

Get all states: A Python script that lists all states in the database "hbtn_0e_0_usa" using MySQLdb.

Filter states: A Python script that lists all states starting with the letter "N" in the database "hbtn_0e_0_usa" using MySQLdb.

Filter states by user input: A Python script that displays all the states matching the name provided by the user in the "states" table of the database "hbtn_0e_0_usa" using MySQLdb.

SQL Injection: A Python script that lists all the states matching the name provided by the user, avoiding SQL injection vulnerabilities.

Cities by states: A Python script that lists all cities in the database "hbtn_0e_4_usa" using MySQLdb.

All cities by state: A Python script that lists all cities of a given state in the database "hbtn_0e_4_usa" using MySQLdb.

First state model: A Python module that defines a class "State" that inherits from SQLAlchemy Base and links to the MySQL table "states".

All states via SQLAlchemy: A Python script that lists all State objects from the database "hbtn_0e_6_usa" using SQLAlchemy.

First state: A Python script that prints the first State object from the database "hbtn_0e_6_usa" ordered by states.id.

Contains a: A Python script that lists all State objects that contain the letter "a" in the database "hbtn_0e_6_usa" using SQLAlchemy.

Get a state: A Python script that prints the id of the State object with the name matching that passed as argument in the database "hbtn_0e_6_usa" using SQLAlchemy.

Add a new state: A Python script that adds the State object "Louisiana" to the database "hbtn_0e_6_usa" using SQLAlchemy.

Update a state: A Python script that changes the name of the State object with id = 2 in the database "hbtn_0e_6_usa" to "New Mexico" using SQLAlchemy.

Delete states: A Python script that deletes all State objects with a name containing the letter "a" from the database "hbtn_0e_6_usa" using SQLAlchemy.

City relationship: A Python module that defines a class "City" that inherits from SQLAlchemy Base and links to the MySQL table "cities". It includes a class attribute "state_id" that is a foreign key to "states.id".


Note: Each task requires running a Python script with a specific set of arguments to execute the relevant database operation.

Conclusion:
This project provides an overview of object-relational mapping and how to use it to perform database operations with MySQL databases. It also provides an understanding of how to use MySQLdb and SQLAlchemy libraries to interact with the database.
