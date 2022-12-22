#simple func

'''def simple_func():
    print('CHECKING...')
simple_func()
'''

'''
def name_param(name):#this is  paramater /works as var..
    print(f'Hello {name}')
name_param('ARYAN') # here ARYAN is argument for ^^^ name_param(name) , in short name=(input)'ARYAN'
'''

'''
def name_param(name):
    print(f'Hello {name}')
name_param('ARYAN') 
name_param('OP')
'''

'''
#FUNCTIONS WITH MORE THEN 1 PARAMETER
def two_par(first_name,frnd_name):
    print(f'hello {first_name} how is {frnd_name}')
two_par('ARYAN' ,'XYZ') #note- in this it is positional sensitive as in paramater order is first_name and frnd_name
two_par(frnd_name='XYZ',first_name='ARYAN') # to change positional arguments'''


'''
def func4(some_argument):
    print(some_argument)
    print(f"{some_argument}is still in this func")
f= func4("NOOB")
'''

'''
OPTINAL PARAMATERS:-   BY =/DEFINING PARAMETER A VARIABLE 

we can provide a default , it will only take default value if argument isn't defined 
note:- if a argument is defined so it will take argument value..
'''
def product(n1,n2=3):
    return n1*n2

print(product(5,5)) #print(product(5))


def optional_para(x1=5):
    print(x1)
optional_para()

def no_of_greet(name,total_greeting=5):
    print(name* total_greeting)
no_of_greet('Aryan ')



"""
def avg(*args):
    total=0
    print(args)
    for i in args:
        total+=i
        print('avg is',total/len(args))

avg(10,22,12,34)
"""

def name(**name):
    print("Hello",name['fname'],name['mname'],name['lname'])

name(mname='xyz',lname='Jain',fname='Aryan')