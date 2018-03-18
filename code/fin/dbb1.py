#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("97.74.4.170","vpssensorfaucets","ZzLpAui!23","vpssenso_stoke_db" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database
sqlstmt = "SELECT * FROM data_table"

try:
   results = cursor.fetchall()
   for row in results:
      print row
except:
   print "Error: unable to fecth data"

cursor.close()
# disconnect from server
db.close()

sys.exit()
