def cr_table(cursor):
	import front as frnts
	a = str(input("Enter the name of table to create:"))
	
	cursor.execute("CREATE TABLE %s (name varchar(20));" %a)
	print("The %s table has been created.")

	condtn = input("Do yo want to exit? 1.Yes")
	if b == 1:
		exit()
	else :
		frnts.front(cursor)

	
