def cr_table(cursor):
	import front as frnts
	a = input("Enter the name of the classroom to create:")
	
	cursor.execute("CREATE TABLE %s (name varchar(40), totalattendance INTEGER );" %a)
	print("The %s classroom table has been created.")
	cursor.execute("COMMIT WORK;")

	condtn = input("*****Press any number to return to the main menu*****")
	if condtn == 1:
		exit()
	else :
		frnts.front(cursor)

	
