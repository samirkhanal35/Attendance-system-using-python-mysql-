def update(cursor):
	b=0
	import front as frnts

	cursor.execute("COMMIT WORK;")
	condtn = input("Do yo want to exit? 1.Yes 2.Noz")
	if b == 1:
		exit()
	else :
		frnts.front(cursor)

