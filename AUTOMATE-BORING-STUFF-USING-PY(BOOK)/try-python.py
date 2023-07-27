'''
class Employee():
    def __repr__(self):
        return f"doesnt matter yaar {self.f_name}"

emp1=Employee()
emp2=Employee()

emp1.f_name='Aryan'
emp1.l_name='Jain'
emp2.f_name=''
emp2.l_name=''
print(emp1,emp1.f_name,emp1.l_name,emp2.f_name)
'''

'''
class Employee():
    def __init__(self,f_name,l_name):
        self.f_name=f_name
        self.l_name=l_name

    def __repr__(self):
        return f"fname -{self.f_name} l-name- {self.l_name} "

    @property
    def info(self):
        return f"{self.f_name}"

emp1=Employee("Aryan","Jain")
print(emp1,emp1.info)
'''

'''

class Employee():
    def __init__(self,f_name,l_name):
        self.f_name=f_name
        self.l_name=l_name

    def __repr__(self):
        return f"fname -{self.f_name} l-name- {self.l_name} "

    @property
    def info(self):
        return f"{self.f_name}"

emp1=Employee("Aryan","Jain")
print(emp1,emp1.info)

class Naukar(Employee):

    def __init__(self, f_name, l_name,work):
        super().__init__(f_name, l_name)
        self.work=work

    def __repr__(self):
        return f"{self.work}"

emp2=Naukar("Noob","Aryan",'good for nthg')
print(emp2.info,emp2.f_name)
print(emp2,emp2.work)
'''



'''import mysql.connector
db=mysql.connector.connect(host='localhost',user='root',passwd='puspa456',database='testin')
mycursor=db.cursor()'''
#mycursor.execute('CREATE DATABASE testin')
#mycursor.execute('CREATE TABLE Info(name VARCHAR(50))')
'''
mycursor.execute('DESCRIBE Info')
for x1 in mycursor:
    print(x1)
'''
#mycursor.execute('ALTER TABLE Info ADD COLUMN (age smallint UNSIGNED)') #ADD,CHANGE,DROP are the operation on ALTER
#db.commit()

#mycursor.execute('INSERT INTO Info(name,age) VALUES (%s,%s)',('NOOB',17))
#db.commit()
'''
mycursor.execute('SELECT * FROM Info')
for rows in mycursor:
    print(rows)
'''



'''with open('xyz.txt','w') as file:
    x1=input('likh')
    read=file.write(x1)'''
'''with open('xyz.txt','r') as file2:
    x2=file2.read()
    print(x2)'''
'''
with open('xyz.txt','a') as file3:
    x3=file3.writelines('HMM')
    x4=file3.write('HMM') #works same as writelines
'''
