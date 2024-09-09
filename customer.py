import mysql.connector as mc
def addCustomer(sqlConnector):
    cursor = sqlConnector.cursor()
    try:
        id = str(input('Enter ID: '))
        firstname = str(input('Enter first name: '))
        lastname = str(input('Enter last name: '))
        date_of_birth = str(input('Enter date_of_birth: '))
        aadhar = str(input('Enter aadhar number: '))
        mobile = str(input ('Enter mobile number: '))
        address = str(input('Enter address: '))
        job = str(input('Enter Job: '))
        query = "insert into customers values ("+id+",'"+firstname+"','"+lastname+"','"+date_of_birth+"','"+aadhar+"',"+mobile+",'"+address+"','"+job+"');"
        print(query)
        cursor.execute(query)
        sqlConnector.commit()
    except mc.Error:
        print("ERROR IN ADDING CUSTOMER")


def removeCustomer(sqlConnector):
    cursor = sqlConnector.cursor()
    try:
        id = str(input('Enter ID: '))
        query = "delete from customers where id ="+id+";"
        print(query)
        cursor.execute(query)
        sqlConnector.commit()
    except mc.Error:
        print("ERROR IN DELETING CUSTOMER")

def start(sqlConnector):
    print('\t\t1. Add Customer')
    print('\t\t2. Remove Customer')
    print('\t\t3. Exit')
    userinput = int(input('\nEnter your input: '))
    if userinput == 1:
        addCustomer(sqlConnector)
        pass
    elif userinput == 2:
        removeCustomer(sqlConnector)
        pass
    elif userinput == 3:
        pass
    else:
        print('Wrong Input Entered. Try again.\n\n')
        start(sqlConnector)
