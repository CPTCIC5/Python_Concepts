#lists are mutable values which store data in the form of discreate elements
#mutuable means we can change data 

'''item=[2,3,4,5,4]
print(item)
'''

'''
l1=['a','b','c']
l1[0]='oe'
print(l1) #this is example 0f mutable , we can change value.. so it will print ['oe','b','c'] 
#instead of ['a','b','c']
'''

'''
item=['XYZ','TOMATO','POTATO','ONION',9]
print(item)
print(len(item))
print(type(item)) #list
print(item[::]) #:it take whole list as default :==default
print(item[-2:]) #anticlockwise prints the item by command "-"
item[0]='xxz'  # changes/edit value of XYZ (1st argument to  xxz)
print(item)#^^
'''

'''
#creating lists/typecasting
x1='hello'
l1=list(x1)
print(x1)

x2={'Aryan':'Op','expect-him':"noob"}
x3=list(x2)
print(x3)

x5=('a','r','y','a','n')
x6=list(x5)
print(x6)
'''

'''
#lists input

x1=list(input('Name'))
print(x1)  #input -Aryan , result == ['a', 'r', 'y', 'a', 'n']

x2=eval(input('Namezz'))
print(x2) #input ['a', 'r', 'y', 'a', 'n'] , result == ['a', 'r', 'y', 'a', 'n']
'''

'''
2D LISTS/NESTED LISTS
a1=[
    ['item1','item2','item3'],
    ['item6','item7','item5']
]
print(a1[0][1]) #it opens list no.1^^ the upper list item 2  here first 0=selection of list one and second = retrieving item no.1(two)
print(a1[0:2]) '''


'''
n1=[5,2,1,6,7]
n1.append(20)         #append add value to that list in last 
n1.insert(0,69) #insert func asks to add a new value same as append but it asks to append where here 0= where u want to insert value
n1.pop()  #removes last value of list
n1.clear() #remove whole list
n1.remove(5)  #removes given value

n2=[5,'aryan']  #a new list
n1.extend(n2)   #appends n2 inside n1

print(n1)
'''


'''
n1=[5,7,9,2,1,3]
n1.sort()  #sorts
n1.reverse() 
print(n1[0])
print(n1)
'''
'''
x1=['hey',5]
x2=['uuf','hmm']
x1.extend(x2)
print(x1)
'''
#REPLICATING/STEALING ANY LIST

'''
n1=[4,8.2,9,54,11,69]
n2=n1.copy()
print(n2)
'''

#UNPACKING
'''n1=['ARYAN','OP']
x,y=n1
print(x)'''


'''
n1=[3,4,4]
print(n1)
n2= sum(n1,10)
print(n2)
'''

'''
#COMPARISION OF LISTS
n1=[1,2,3]
n2=[1,2,3]
print(n1==n2)

n3=[1,2,3]
n4=[1,[2,3]]
print(n3==n4)

n5=[1,2,3]
n6=['1','2','3']
print(n5==n6)
'''

'''
#concatanation of lists

x1=['a','b','c']
x2=[1,2,3]
print(x1+x2)
'''

'''
import random
messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])
'''