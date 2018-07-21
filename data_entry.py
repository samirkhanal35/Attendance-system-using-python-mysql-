def entry(cursor):
	a = str(input("Enter the table name to enter values:"))
	name = str(input("Enter the name of student:"))
	cursor.execute("INSERT INTO samir VALUES ( 'samir' );")
	cursor.execute("INSERT INTO samir VALUES ( 'sam' );")
	cursor.execute("INSERT INTO samir VALUES ( 'sir' );")
