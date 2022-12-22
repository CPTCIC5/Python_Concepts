#map

li=[1,2,4,5,6,7,8,9,10]

def func(x):
    return x**x

print(list(map(func,li)))

#filter

def isOdd(x):
    return x%2 != 0

a=[1,2,3,4,5,6,7,8,9,10]
b= list(filter(isOdd,a)) #filters/dumps only True objects from function passed inside filter into variable
c= list(map(isOdd,filter(isOdd,a)))