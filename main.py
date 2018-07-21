def main(cursor,a):
	import attendance as atd
	import cr_table as crt
	import del_table as delt
	import data_entry as datae
	import show_attendance as shwatd
	import update_attendance as updatd
	import front as frnts
	import os
	#os.system("clear")
	if a == 1:
		atd
	elif a == 2:
		crt.cr_table(cursor)
	elif a == 3:
		datae.entry(cursor)
	elif a == 4:
		delt
	elif a == 5:
		shwatd.show(cursor)
	elif a == 6:
		updatd
	elif a == 7:
		exit()
	else :
		
		frnts.front()
