def attendance(cursor):
    condtn = 0
    import front as frnts
    c = str(input("Enter the class name to take attendance from:"))
    cursor.execute("SELECT * FROM %s;" %c)

    result = cursor.fetchall()

    a = len(result)

    while a>0 :
        de = result[(a-1)]
        b = int(input("Is "+de[0]+" present? 1. Yes 2. No"))

        if b==1 :
            cursor.execute("UPDATE "+c+" SET totalattendance=totalattendance+1 WHERE name = '%s';" %de[0])
        a=a-1

    cursor.execute("COMMIT WORK;")
    condtn = input("*****Press any number to return to the main menu*****")
    if condtn == 1:
        exit()
    else :
        frnts.front(cursor)



