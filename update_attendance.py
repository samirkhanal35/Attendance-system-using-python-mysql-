def update(cursor):
    b=0
    import front as frnts
    a = str(input("Enter the class room name to be updated:"))
    cursor.execute("SELECT * FROM %s;" %a)
    result = cursor.fetchall()
    #de = result[2]
    #print(de[0])
    for row in result:
        print (row[0],row[1])

    de = str(input("Enter the name of student to change attendance:"))
    #df = int(input("Enter the attendance to be updated of %s :" %de))
    lp = int(input("Enter \n1. To increase attendance by 1 \n 2. To decrease attendance by 1:"))
    if lp == 1:
        cursor.execute("UPDATE "+a+" SET totalattendance=totalattendance+1 WHERE name = '%s';" %de[0] )
        cursor.execute("COMMIT WORK;")
        print("Attendance has been incresed by ones")
    elif lp == 2:
        cursor.execute("UPDATE "+a+" SET totalattendance=totalattendance-1 WHERE name = '%s';" %de[0] )
        cursor.execute("COMMIT WORK;")
        print("Attendance has been decreased by one")
    else :
        print("\n****Invalid input****")

    cursor.execute("COMMIT WORK;")
    condtn = input("*****Press any number to return to the main menu*****")
    if b == 1:
        exit()
    else :
        frnts.front(cursor)

