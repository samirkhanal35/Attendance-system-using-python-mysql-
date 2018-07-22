def show_table(cursor):
    import front as frnts
    cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE'")
    result = cursor.fetchall()

    print("**** Tables present in Database ****\n")
    print(result[0],end=" ")
    print("\n")




    condtn = 0


    cursor.execute("COMMIT WORK;")
    condtn = int(input("Do yo want to exit? 1.Yes"))
    if condtn == 1:
        exit()
    else :
        frnts.front(cursor)
