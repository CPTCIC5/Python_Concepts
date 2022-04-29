#generators r objects which geberate value on-fly
'''def sum(limit):
    for i in range(limit):
        yield i

x1=sum(69696969)
print(x1)'''


def gen(n):
    for i in range(n):
        yield i 

g = gen(3)
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