import time
import threading
from concurrent.futures import ThreadPoolExecutor
import asyncio

"""
#manually
def func1(seconds):
    print(f'sleeping for {seconds} seconds')
    time.sleep(seconds)


func1(5)
func1(2)
func1(3)
"""

"""
#via async way (reducing time/optimizing function runtime/finish time)
async def func1(seconds):
    print(f'sleeping for {seconds} seconds')
    await asyncio.sleep(seconds)

async def main():
    task= asyncio.create_task(func1(5))
    task2= asyncio.create_task(func1(2))
    task3= asyncio.create_task(func1(3))
    await task
    await task2
    await task3

asyncio.run(main())
"""

def func1(seconds):
    print(f'sleeping for {seconds} seconds')
    time.sleep(seconds)


t1=threading.Thread(target=func1,args=[5])
t2=threading.Thread(target=func1,args=[2])
t3=threading.Thread(target=func1,args=[3])

#start the function in 0 secs (on the fly)
t1.start()
t2.start()
t3.start()
#wait until the highest time taking command executes
t1.join()
t2.join()
t3.join()


def poolingDemo():
    with ThreadPoolExecutor() as executor:
        l=[3,5,2,1]
        results = executor.map(func1,l)
        for result in results:
            print(result)
