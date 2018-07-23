def delete(cursor):
	import front as frnts
	a = str(input("Enter the name of class room to delete:"))


	cursor.execute("DROP TABLE %s ;" %a)
	print("The %s class room table has been deleted." %a)
	cursor.execute("COMMIT WORK;")


	condtn = input("*****Press any number to return to the main menu*****")
	if condtn == 1:
		exit()
	else :
		frnts.front(cursor)





	#frnts.front(cursor)






