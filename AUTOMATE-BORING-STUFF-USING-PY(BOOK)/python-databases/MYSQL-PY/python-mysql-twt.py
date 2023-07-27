import mysql.connector

db= mysql.connector.connect(host='localhost',username='root',database='AryanTesting')
mycursor=db.cursor()

#mycursor.execute("CREATE DATABASE AryanTesting")
#mycursor.execute("CREATE TABLE Hospital (name VARCHAR(50),age smallint UNSIGNED,id int PRIMARY KEY AUTO_INCREMENT) ")

#mycursor.execute("INSERT INTO Hospital (name,age) VALUES (%s,%s)",("Noob",100))
#mycursor.
#db.commit()

#mycursor.execute("SELECT * FROM Hospital WHERE id=6")
#print(mycursor.fetchone())
#for x in mycursor:
#    print(x)

#mycursor.execute("ALTER TABLE Hospital ADD COLUMN (username VARCHAR(20)) ")
#mycursor.execute("ALTER TABLE Hospital CHANGE username  changedusername VARCHAR(4) ")
#mycursor.execute('DESCRIBE Hospital')
#for i in mycursor:
#    print(i)

mycursor.execute("CREATE TABLE Patient(id int,FOREIGN KEY (id) REFERENCES Hospital(id))")
mycursor.execute("DESCRIBE Patient")
for data in mycursor:
    print(data)