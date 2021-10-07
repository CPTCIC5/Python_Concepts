'''item=[2,3,4,5,4]
print(item)
'''


'''
item=['XYZ','TOMATO','POTATO','ONION',9]
print(item)
print(len(item))
print(type(item)) #list
print(item[::]) #:it take whole list as default :==default
print(item[-2:]) #anticlockwise prints the item by command "-"
item[0]='xxz'  # changes value of XYZ (1st argument to  xxz)
print(item)#^^
'''

'''
2D LISTS
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
print(n1)
'''


'''
n1=[4,8.2,9,54,11,69]
n1.sort()  #sorts 
n1.reverse()   #reverse-sorting
print(n1)
'''

#REPLICATING ANY LIST

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

n=int(input())
while i in range(n):
    i=0
    print(i+1,end="")