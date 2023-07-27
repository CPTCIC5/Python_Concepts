import requests
"""
url = requests.get('https://httpbin.org')
print(url.ok)
print(url.headers)
print(url.status_code)
"""

r= requests.get('https://httpbin.org/get') #get is a slug defined 
print(r.json())
#slug as a param for handling it via requests library 
payload={'page':2,'count':25}
r2=requests.get('https://httpbin.org/get',params=payload)
print(r2.url)
print(r2.json())


payload2={'usename':'aryan','password':'puspa456'}
r3=requests.post('https://httpbin.org/post',params=payload2)
print(r3.json())

r4=requests.get('https://httpbin.org/basic-auth/corey/testing',auth=('aryan','puspa456'))