"""
import asyncio

async def main():
    print('xyz')

async def foo(text):
    print(text)
    await asyncio.sleep(1)

asyncio.run(main())
"""

import asyncio
import requests
import time
#saving img
url = "http://craphound.com/images/1006884_2adf8fc7.jpg"
response = requests.get(url)
#if response.status_code == 200:

async def func1():
    with open("sample.jpg", 'wb') as f:
        f.write(response.content)
        await asyncio.sleep(1)

async def func2():
    with open("sample2.jpg", 'wb') as f:
        f.write(response.content)
        await asyncio.sleep(1)

async def func3():
    with open("sample3.jpg", 'wb') as f:
        f.write(response.content)
        await asyncio.sleep(3)


"""
async def main():
    task3=asyncio.create_task(func3())
    print(f"started at {time.strftime('%X')}")
    await func1()
    await func2()
    await task3
    print(f"finished at {time.strftime('%X')}")
"""

#another method can  be
async def main():
    tasks=asyncio.gather(
        func1(),
        func2(),
        func3()
    )
    print(f"started at {time.strftime('%X')}")
    await tasks
    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
