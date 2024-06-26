import pymysql

dataBase = pymysql.connect(
    host='localhost',
    user='root',
    password='password123'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE cropStorage")

print("Database created")
