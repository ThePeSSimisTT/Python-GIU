import mysql.connector
from mysql.connector import errorcode


def DatabaseConnectionError():
    try:
      cnx = mysql.connector.connect(host='127.0.0.1',
                                    database='autonebg',
                                    user='root',
                                    password='1234')
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)
    else:
          print("we gud")
          return cnx
          

