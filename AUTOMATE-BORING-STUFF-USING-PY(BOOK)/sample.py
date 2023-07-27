from bs4 import BeautifulSoup

with open("sample.html","r") as f:
    html_doc= f.read() #html to str


soup= BeautifulSoup(html_doc,'html.parser')


#BASICS
"""
print(soup.div)
print(soup.find_all('div')[0])
for link in soup.find_all("a"):
    #print('mili',link)
    print('mili',link.get("href"))
    print("got",link.get_text())

s= soup.find(id='link3')
print(s)
print(s.get('href'))
"""

#selector = ./#
#prefix = class_/id


#FILTER AND PARENTING
"""
print(soup.select('div.italic')) #class
#or
print(soup.find(class_='italic')) #as in list

print(soup.select('div#italic')) #id
#or
print(soup.find(id='italic'))# as in list

#for child in soup.find(id="container").children:
    #print(child)

for parent  in  soup.find(class_='box').parents:
    print(parent)
"""

#CREATE/UPDATE
#update
change= soup.find(class_="changeme")
change.name='xyz'
print(change.name)
