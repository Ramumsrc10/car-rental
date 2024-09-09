from myModules import sqlConnector
from myModules import startPage
from myModules import customer
from myModules import car
from myModules import rentOrReturn
from myModules import information

sqlConnect = sqlConnector.connect()

while sqlConnect:
    user_input = startPage.start('Dexian Car Rentals')
    if user_input ==1:
        customer.start(sqlConnect)
    elif user_input ==2:
        car.start(sqlConnect)
    elif user_input ==3:
        rentOrReturn.start(sqlConnect)
    elif user_input ==4:
        information.start(sqlConnect)
    else:
        break
