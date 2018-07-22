def show(cursor):
	b=0
	import front as frnts
	a = str(input("Enter the table name to be displayed:"))






	cursor.execute("SELECT * FROM %s;" %a)
	result = cursor.fetchall()
	for row in result:
		print (row[0],row[1])

	cursor.execute("COMMIT WORK;")
	condtn = input("Do yo want to exit? 1.Yes 2.No")
	if condtn == 1:
		exit()
	else :
		frnts.front(cursor)

		'''

	for i in range(cursor.rowcount):
		row = cursor.fetchone()
		print (row[0])

	#cursor.execute("rollback")'''
		#frnts.front(cursor)
