def entry(cursor):
	import front as frnts
	condtn = 0

	a = str(input("Enter the class room name to enter values:"))
	i = 1
	while (i == 1):
		b = str(input("Enter the name of student:"))
		cursor.execute("INSERT INTO "+a+" VALUES ( '%s' , 0);" %b)
		i = int(input("Do you want to add another name? 1.Yes 2.No"))


	cursor.execute("COMMIT WORK;")
	condtn = input("*****Press any number to return to the main menu*****")
	if condtn == 1:
		exit()
	else :
		frnts.front(cursor)



	'''name = str(input("Enter the name of student:"))

	cursor.execute("INSERT INTO samir VALUES ( 'samir' );")
	cursor.execute("INSERT INTO samir VALUES ( 'sam' );")
	cursor.execute("INSERT INTO samir VALUES ( 'sir' );")
	'''





	#frnts.front(cursor)
