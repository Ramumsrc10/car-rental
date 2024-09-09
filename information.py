import mysql.connector as mc
def customerInfo(sqlConnector):
    cursor = sqlConnector.cursor()
    try:
        id = str(input('Enter ID: '))
        query = "select * from customers where id = "+id+";"
        print(query)
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
    except mc.Error:
        print("ERROR IN FETCHING CUSTOMER INFO")

def carInfo(sqlConnector):
    cursor = sqlConnector.cursor()
    try:
        id = str(input('Enter ID: '))
        query = "select * from cars where id = "+id+";"
        print(query)
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
    except mc.Error:
        print("ERROR IN FETCHING CAR INFO")

def start(sqlConnector):
    print('\t\t1. Customer Info')
    print('\t\t2. Car Info')
    print('\t\t3. Exit')
    userinput = int(input('\nEnter your input: '))
    if userinput == 1:
        customerInfo(sqlConnector)
    elif userinput == 2:
        carInfo(sqlConnector)
    elif userinput == 3:
        pass
    else:
        print('Wrong Input Entered. Try again.\n\n')
        start(sqlConnector)
