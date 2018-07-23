def show_table(cursor):
    import front as frnts
    cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE'")
    result = cursor.fetchall()

    print("**** Tables present in Database ****\n")

    a= len(result) - 121

    for i in range(0,a):
        print(result[i],end=" ")
        print("\n")

    condtn = 0


    cursor.execute("COMMIT WORK;")
    condtn = int(input("*****Press any number to return to the main menu*****"))
    if condtn == 1:
        exit()
    else :
        frnts.front(cursor)
