import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'wontoPNA2383LS@#f*!FL',
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE elderco")
dataBase.commit()
print("All done")