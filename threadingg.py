import threading
import time

"""
def func():
    print('hemlo')
    time.sleep(1)
    print('done')
    time.sleep(0.85)
    print('now done')

x=threading.Thread(target=func)
x.start()
print(threading.activeCount())
time.sleep(1)
print('finally')
"""


"""def greet(name):
    print(name)
    time.sleep(1)
    print('done')

x2= threading.Thread(target=greet, args=('aryan', ))
x2.start()"""



"""def count(n):
    for i in range(1,n+1):
        print(i)
        time.sleep(0.01)


def count2(n):
    for i in range(1,n+1):
        print(i)
        time.sleep(0.01)"""

ls = []
def count(n):
    for i in range(1,n+1):
        ls.append(i)
        time.sleep(0.01)


def count2(n):
    for i in range(1,n+1):
        ls.append(i)
        time.sleep(0.01)

x = threading.Thread(target=count, args=(3,))
x.start()
x.join() #to join or run syncronously
y = threading.Thread(target=count2, args=(5,))
y.start()
print(ls)