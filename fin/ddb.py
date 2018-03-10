#!/usr/bin/python
# view_rows.py - Fetch and display the rows from a MySQL database query

# import the MySQLdb and sys modules
import MySQLdb
import sys

# open a database connection
# be sure to change the host IP address, username, password and database name to match your own
connection = MySQLdb.connect (host = "97.74.4.170", user = "vpssensorfaucets", passwd = "ZzLpAui!23", db = "vpssenso_stoke_db")

# prepare a cursor object using cursor() method
cursor = connection.cursor ()

# execute the SQL query using execute() method.
cursor.execute ("select * from 'machine_check'")

# fetch all of the rows from the query
data = cursor.fetchall ()

# print the rows
#for row in data :
#print row[0], row[1]
while 1:
	print data

# close the cursor object
cursor.close ()

# close the connection
connection.close ()

# exit the program
sys.exit()

