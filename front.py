#!/usr/bin/python

def front(cursor):
	import front as frnts
	import attendance as atd
	import cr_table as crt
	import del_table as delt
	import data_entry as datae
	import show_attendance as shwatd
	import update_attendance as updatd
	import main as mn


	import os
	os.system("clear")



	print("\t******Attendance System******\n") #.center(150)
	print("\t 1.Take Attendance\n")
	print("\t 2.Create classroom\n")
	print("\t 3.Enter Students names\n")
	print("\t 4.Delete classroom\n")
	print("\t 5.Show Attendance\n")
	print("\t 6.Update Attendance\n")
	print("\t 7.Show classrooms\n")
	print("\t 8.Exit\n")
	a = int(input("\t Select your choice: "))
	mn.main(cursor,a)
	

	#os.system("clear")

								



	#print(a)
	#frnts.front(cursor)
