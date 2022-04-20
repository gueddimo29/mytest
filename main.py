import mysql.connector
db = mysql.connector.connect(host="localhost",
                             user="root",
                             password="azertyuiop.123",
                             database="testDB")

cursor = db.cursor()
cursor.execute("SELECT * FROM users")
myResult = cursor.fetchall()

# thank you this is me again
for xx in myResult:
    print(xx)

