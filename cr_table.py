def cr_table(cursor):
	a = str(input("Enter the name of table to create:"))
	
	cursor.execute("CREATE TABLE %s (name varchar(20));" %a)
	
