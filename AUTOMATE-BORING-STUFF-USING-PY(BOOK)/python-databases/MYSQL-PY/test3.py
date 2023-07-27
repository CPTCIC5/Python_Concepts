import mysql.connector

db=mysql.connector.connect(host='localhost',user='root',passwd='puspa456',database='Factory')
mycursor=db.cursor()
#mycursor.execute("CREATE DATABASE Factory")
#mycursor.execute("CREATE TABLE Worker(ecode smallint UNSIGNED NOT NULL,name VARCHAR(50)NOT NULL,design VARCHAR(30) NOT NULL,plevel VARCHAR(4) NOT NULL,doj DATE,dob DATE)")
'''
mycursor.execute("DESCRIBE Worker")
for table in mycursor:
    print(table)
'''
#mycursor.execute('ALTER TABLE Worker CHANGE COLUMN plevel plevel VARCHAR(4) NOT NULL')

mycursor.execute("INSERT INTO Worker(ecode,name,design,plevel,doj,dob) VALUES (%s,%s,%s,%s,%s,%s),(%s,%s,%s,%s,%s,%s),(%s,%s,%s,%s,%s,%s),(%s,%s,%s,%s,%s,%s),(%s,%s,%s,%s,%s,%s)", 
(11,"Radhe Shyam","Supervisor","POO1","2004-Sept-13","1981-Aug-23"),(12,"Chander Nath","Operator","P003","2010-Feb-22","1987-Jul-12"),(13,"Fizza","Operator","POO3","2009-Jun-14"),
(15,"Ameen Ahmed","Mechanic","POO2","2006-Aug-21","1984-Mar-13"),(18,"Sanya","Clerk","P002","2005-Dec-19","1983-Jun-09"))
db.commit()