import mysql.connector as mc
def addCar(sqlConnector):
    cursor = sqlConnector.cursor()
    try:
        id = str(input('Enter ID: '))
        company = str(input('Enter company name: '))
        model = str(input('Enter model name: '))
        YOP = str(input('Enter year of purchase: '))
        platenumber = str(input('Enter plate number: '))
        fueltype = str(input ('Enter fueltype: '))
        gear = str(input('Enter no. of gears: '))
        engine_power = str(input('Enter engine power: '))
        seat = str(input('Enter no. of seats: '))
        drp = str(input('Enter rent per day: '))
        query = "insert into cars values ("+id+",'"+company+"','"+model+"',"+YOP+",'"+platenumber+"','"+fueltype+"',"+gear+","+engine_power+","+seat+","+drp+","+"0,'A');"
        print(query)
        cursor.execute(query)
        sqlConnector.commit()
    except mc.Error:
        print("ERROR IN ADDING CUSTOMER")


def removeCar(sqlConnector):
    cursor = sqlConnector.cursor()
    try:
        id = str(input('Enter ID: '))
        query = "delete from cars where id ="+id+";"
        print(query)
        cursor.execute(query)
        sqlConnector.commit()
    except mc.Error:
        print("ERROR IN DELETING CAR")


def start(sqlConnector):
    print('\t\t1. Add the Car')
    print('\t\t2. Remove the Car')
    print('\t\t3. Exit from rental')
    userinput = int(input('\nEnter your input: '))
    if userinput == 1:
        addCar(sqlConnector)
    elif userinput == 2:
        removeCar(sqlConnector)
        pass
    elif userinput == 3:
        pass
    else:
        print('Wrong Input Entered. Try again.\n\n')
        start(sqlConnector)
