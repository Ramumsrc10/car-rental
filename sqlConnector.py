import mysql.connector as mc
def connect ():
    username = input('Enter mysql username : ')
    password = input('Enter mysql password : ')
    database = input('Enter database name : ')
    try:
        mydb = mc.connect(
            host="localhost",
            user=username,
            password=password,
            database=database
        )
        print('Database Connected Successfully.\n\n')
        return mydb
    except mc.Error:
        print("ERROR IN CONNECTION")
        return connect()