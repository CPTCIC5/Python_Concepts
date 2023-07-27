import mysql.connector

db = mysql.connector.connect(host="localhost",user="root",passwd="puspa456",database="testdatabase") #used to connect db with the credenatials
mycursor = db.cursor() # to curse/preview make/change stuff inside a db

#mycursor.execute("CREATE DATABASE testdatabase") # a different way used to create a new db

#CREATING TABLE
#mycursor.execute("CREATE TABLE  Person(name VARCHAR(50),age smallint UNSIGNED,personID int PRIMARY KEY AUTO_INCREMENT)") # CREATE TABLE <TABLENAME> (<column>)
#mycursor.execute("DESCRIBE Person") #DESCRIBE  <TABLENAME> --> USED TO PRINT THE QUERY
#for x1 in mycursor:
#    print(x1)

#ADDING QUERIES INSIDE TABLE
#mycursor.execute("INSERT INTO Person(name,age) VALUES (%s,%s)", ("Aryan",18))
#db.commit()

#READ OPERATION TO READ ALL STUFF IN DB
mycursor.execute("SELECT * FROM Person")
for x1 in mycursor:
    print(x1)

