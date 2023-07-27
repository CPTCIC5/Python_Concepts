import requests
from bs4 import BeautifulSoup

"""
url = requests.get('https://zappycode.com/')
#print(url.text,url.url)
#print(url.content)
#print(url.headers)

urlImage= requests.get('https://zappycode.com/static/sitewide/topCourses.png')
#print(urlImage.content)
with open('offer.png','wb') as f:
    f.write(urlImage.content)
"""


"""
payloads={'username':'corey','password':'testing'}
r= requests.post('https://httpbin.org/get',data=payloads)
print(r.json())
"""

#AMAZON
url = 'https://www.amazon.in/s?k=iphone&ref=nb_sb_noss_2'
user_agent = {'User-agent': 'Mozilla/5.0'}

response= requests.get(url,headers=user_agent)

soup=BeautifulSoup(response.text,'html.parser')
print(soup)