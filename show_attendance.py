def show(cursor):
	a = str(input("Enter the table name to be displayed:"))
	cursor.execute("SELECT * FROM %s;"%a)
	result = cursor.fetchall()
	for row in result:
		print (row[0])
	
	'''for i in range(cursor.rowcount):
		row = cursor.fetchone()
		print (row[0], row[1])

	cursor.execute("rollback")'''
