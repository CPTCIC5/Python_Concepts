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