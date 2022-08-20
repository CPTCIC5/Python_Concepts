import mysql.connector

db=mysql.connector.connect(host='localhost',user='root',password='puspa456',database='noob')
mycursor=db.cursor()
mycursor.execute("CREATE TABLE  Person(name VARCHAR(50),age smallint UNSIGNED,personID int PRIMARY KEY AUTO_INCREMENT)")