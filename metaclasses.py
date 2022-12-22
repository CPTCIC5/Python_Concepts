class Foo():
    def speak(self):
        return "FOo says Hi!"
"""
Employee = type('Employee',(),{})
print(type(Employee))
"""

"""
Employee = type('Employee',(),{'x':5})
print(Employee.x)
"""

Employee = type('Employee',(Foo,),{'x':5})

x=Employee()
print(x.speak())