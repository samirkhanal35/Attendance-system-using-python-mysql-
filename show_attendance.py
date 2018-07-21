def show(cursor):
	a = str(input("Enter the table name to be displayed:"))
	cursor.execute("SELECT * FROM samir);")
	
	'''for i in range(cursor.rowcount):
		row = cursor.fetchone()
		print (row[0], row[1])...
