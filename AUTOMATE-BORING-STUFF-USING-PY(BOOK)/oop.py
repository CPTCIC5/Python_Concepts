"""
class Dog:
    def __init__(self,name,age):
        print('trigger huwa')
        self.name=name
        self.age=age
        self.li=[1,2,3]
    
    def speak(self):
        print('Hi i m',self.name,'my age is',self.age)

    def edit_age(self,age):
        self.age=age

    def address(self,addresss):
        self.addresss=addresss

dog1=Dog('Aryan',18)
dog2=Dog('Noob',19)

print(dog1.age)
dog1.edit_age(11)
print(dog1.age)
dog1.address('CP')
print(dog1.addresss)


class Cat(Dog):
    def __init__(self, name, age,color):
        super().__init__(name, age)
        self.color=color
    def meow(self):
        return self.color

tim=Cat('aryan',5,'blue')

tim.edit_age(111)
print(tim.age)
tim.address('UK')
print(tim.addresss)
print(tim.meow())
"""

"""
class Point():
    def __init__(self,x=0,y=0):
        self.x=0
        self.y=0
        self.coords= (self.x,self.y)
        
    def move(self,x,y):
        self.x+=x
        self.y+=y

    def __add__(self,p):
        return Point(self.x +p.x ,self.y +p.y)
    
    def __subtract__(self,p):
        return Point(self.x -p.x ,self.y -p.y)
    
    def __mul__(self,p):    
        return Point(self.x *p.x ,self.y *p.y)
    def __str__(self,p):
        return Point(str(self.x) + str(self.y))
        
x1=(1,1)
x2=(2,3)
x3=(2,1)
x4=(3,2)
"""