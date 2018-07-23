import front as frnts

import MySQLdb
import os

# Open database connection
db = MySQLdb.connect("localhost","samir","sk","attendance" )

# prepare a cursor object using cursor() method
cursor = db.cursor()



frnts.front(cursor)



# execute SQL query using execute() method.
#cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
#data = cursor.fetchone()
#print ("Database version : %s " % data)

# disconnect from server
db.close()



