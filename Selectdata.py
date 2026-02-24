
import mysql.connector

conn = mysql.connector.connect(host = 'localhost', user = 'root', password = 'Root@12345', database = 'pythondb')

if conn.is_connected():
    print('connection established')

mycursor = conn.cursor()

mycursor.execute('select * from student')

rows = mycursor.fetchall()

for row in rows:
    print(row)
# mycursor.execute('select * from student')