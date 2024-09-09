import mysql.connector as mc
def rentCar(sqlConnector):
    cursor = sqlConnector.cursor()
    try:
        query = "select id,firstname, lastname,aadhar from customers;"
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
        customerinput = str(input('\n:Enter Customer id: '))
        query = "select id,company, model,platenumber,seat,fueltype, drp from cars where availability='A';"
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
        carinput = str(input('\n:Enter Car id: '))
        date_of_rent = input('\nEnter the date of rent: ')
        query = "insert into rental values ("+customerinput+","+carinput+",'"+date_of_rent+"');"
        print(query)
        cursor.execute(query)
        sqlConnector.commit()
        query = "update cars set availability = 'NA' where id ="+carinput+";"
        print(query)
        cursor.execute(query)
        sqlConnector.commit()
    except mc.Error:
        print("ERROR IN ADDING RENTAL")


def returnCar(sqlConnector):
    cursor = sqlConnector.cursor()
    try:
        customerinput = str(input('\n:Enter Customer id: '))
        carinput = str(input('\n:Enter Car id: '))
        date_of_return = input('\nEnter the date of return: ')
        query = "select date_of_rent from rental where customer_id = "+customerinput+" and car_id = "+carinput+";"
        print(query)
        cursor.execute(query)
        result = cursor.fetchall()
        query = "select datediff('"+result[0][0]+"','"+date_of_return+"');"
        cursor.execute(query)
        result = cursor.fetchall()
        days = abs(result[0][0])
        query = "select drp, total_profit from cars where id = "+carinput+";"
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
        drp = abs(result[0][0])
        current_profit = result[0][1]
        rent = days*drp
        print("Total Car rent : "+str(rent))
        payment_status = input("paid? (y/n)")
        if payment_status == 'y':
            query = "update cars set total_profit = "+str(current_profit+rent) +" where id =" + carinput + ";"
            print(query)
            cursor.execute(query)
            sqlConnector.commit()
            query = "update cars set availability = 'A' where id =" + carinput + ";"
            print(query)
            cursor.execute(query)
            sqlConnector.commit()
            query = "delete from rental where customer_id = "+customerinput+" and car_id = "+carinput+";"
            print(query)
            cursor.execute(query)
            sqlConnector.commit()
        else:
            print('pay and return the car.')
    except mc.Error:
        print("ERROR IN RETURNING RENTAL")


def start(sqlConnector):
    print('\t\t1. Rent Car')
    print('\t\t2. Return Car')
    print('\t\t3. Exit')
    userinput = int(input('\nEnter your input: '))
    if userinput == 1:
        rentCar(sqlConnector)
    elif userinput == 2:
        returnCar(sqlConnector)
        pass
    elif userinput == 3:
        pass
    else:
        print('Wrong Input Entered. Try again.\n\n')
        start(sqlConnector)

