def entry(cursor):
	import front as frnts

	a = str(input("Enter the table name to enter values:"))
	i = 1
	while (i == 1):
		b = str(input("Enter the name of student:"))
		cursor.execute("INSERT INTO %a VALUES ( '%b' );" %a %b)
		i = input("Do youu want to add another name? 1.Yes 2.No")


	condtn = input("Do yo want to exit? 1.Yes")
	if b == 1:
		exit()
	else :
		frnts.front(cursor)



	'''name = str(input("Enter the name of student:"))

	cursor.execute("INSERT INTO samir VALUES ( 'samir' );")
	cursor.execute("INSERT INTO samir VALUES ( 'sam' );")
	cursor.execute("INSERT INTO samir VALUES ( 'sir' );")
	'''





	#frnts.front(cursor)
