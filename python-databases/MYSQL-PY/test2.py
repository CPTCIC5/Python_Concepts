import mysql.connector
import datetime

db=mysql.connector.connect(host='localhost',user='root',passwd='puspa456',database='info')
mycursor=db.cursor()

#mycursor.execute('CREATE TABLE Info(name VARCHAR(50) NOT NULL,created datetime NOT NULL,gender ENUM("M","F")NOT NULL,id int PRIMARY KEY AUTO_INCREMENT)')
'''
mycursor.execute("DESCRIBE Info")  #to check columns/class in db/CHECK THE CLASS 
for x in mycursor:
    print(x)
'''

#mycursor.execute("INSERT INTO Info(name,created,gender) VALUES (%s,%s,%s)",('Aryan',datetime.datetime.now(),'M'))
#db.commit()
'''
mycursor.execute("SELECT * FROM info")
for x2 in mycursor:
    print(x2)
'''

#ALTERING -(ADD,DROP,CHANGE)
#mycursor.execute("ALTER TABLE info ADD COLUMN interest VARCHAR(50) NOT NULL")
'''
mycursor.execute("DESCRIBE info")
for x3 in mycursor:
    print(x3)
'''
#mycursor.execute("ALTER TABLE info DROP COLUMN interest")
'''
mycursor.execute("DESCRIBE info")
for x4 in mycursor:
    print(x4)
'''
#mycursor.execute("ALTER TABLE info CHANGE COLUMN created_at created datetime NOT NULL")
'''
mycursor.execute("DESCRIBE info")
for x5 in mycursor:
    print(x5)
'''