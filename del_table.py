def delete(cursor):
	import front as frnts
	a = str(input("Enter the name of table to delete:"))


	cursor.execute("DROP TABLE %s ;" %a)
	print("The %s table has been deleted." %a)


	condtn = input("Do yo want to exit? 1.Yes")
	if condtn == 1:
		exit()
	else :
		frnts.front(cursor)





	#frnts.front(cursor)






