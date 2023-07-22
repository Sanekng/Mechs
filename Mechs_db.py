import mysql.connector
from mysql.connector import Error 


data = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '12345678'
)

cursor_o = data.cursor()
try:
    cursor_o.execute("CREATE DATABASE Mech_parts")
except Error as e:
    print(e)
print('done')