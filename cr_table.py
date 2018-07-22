def cr_table(cursor):
	import front as frnts
	a = input("Enter the name of table to create:")
	
	cursor.execute("CREATE TABLE %s (name varchar(40), totalattendance INTEGER );" %a)
	print("The %s table has been created.")
	cursor.execute("COMMIT WORK;")

	condtn = input("Do yo want to exit? 1.Yes 2.No")
	if condtn == 1:
		exit()
	else :
		frnts.front(cursor)

	
