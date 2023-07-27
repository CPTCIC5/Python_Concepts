#generators r objects which geberate value on-fly
def sum(limit):
    for i in range(limit):
        yield (i)

x1=sum(69696969)
print(x1.__next__())


"""
def gen(n):
    for i in range(n):
        yield i 

g = gen(3)
"""

'''
#print(g)
print(g.__next__())
print(g.__next__())
print(g.__next__())
'''
'''
for iteration in g:
    print(iteration)
'''

#GENERATORS - TECHWITHTIM
"""x = [1,2,3,4,5,6,7,8,9,10]


for element in x:
    print(element)"""

"""for element in range(1,11):
    print(element)"""

x = range(1,11)

print(next(iter(x)))
print(next(iter(x)))



"""
xyz='aryan'
xyz2=iter(xyz)

print(xyz2.__next__())
print(xyz2.__next__())


def gen(n):
    for i in range(n):
        yield i

x=gen(10)
#print(x.__next__())

#for i in x:
#    print(i)
"""


"""
def factorial(n):
    if n<1:
        return 1
    fact=n*factorial(n-1)
    yield fact
#cant be generated as it's a int value
gen = factorial(5)
gen =(iter(gen))
#print(gen.__next__())
"""

def fibonacci(n):
    if n<=1:
        return 1
    else:
        fn=fibonacci(n-1)+fibonacci(n-2)
        yield fn
