def attendance(cursor):
	condtn = 0
	import front as frnts



	cursor.execute("COMMIT WORK;")
	condtn = input("Do yo want to exit? 1.Yes")
	if condtn == 1:
		exit()
	else :
		frnts.front(cursor)



