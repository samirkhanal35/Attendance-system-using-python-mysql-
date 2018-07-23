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
    cursor.execute("UPDATE "+c+" SET totalattendance=totalattendance+1 WHERE name = '%s';" %de[0])
    cursor.execute("COMMIT WORK;")
    condtn = input("*****Press any number to return to the main menu*****")
    if b == 1:
        exit()
    else :
        frnts.front(cursor)

