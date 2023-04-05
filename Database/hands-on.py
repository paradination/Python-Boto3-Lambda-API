import mysql.connector

mydb = mysql.connector.connect(
  host="test-database.c37u8lyxpqob.us-east-1.rds.amazonaws.com",
  user="admin",
  password="Admin12345",
  database="Paradin"
)

print("\n")
#all the fxns applied with the connector
# print(dir(mydb))

mycursor = mydb.cursor()

#all fxns with cursor 
# print("\n for cursor")
# print(dir(mycursor))

mycursor.execute("CREATE DATABASE Paradin")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)

# creating a table in an existing database
mycursor.execute("CREATE TABLE Ikpe (name varchar(10), age varchar(15))")

sql = "INSERT INTO Ikpe (name, age) VALUES (%s , %s)"
val = ("jay", "30")
mycursor.execute(sql, val)

mydb.commit()
print(mycursor.rowcount, "record inserted.")

mycursor.execute("SELECT * FROM Ikpe")

display = mycursor.fetchall()

for items in display:
    print(items)