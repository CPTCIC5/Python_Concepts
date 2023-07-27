import requests,bs4
res = requests.get('https://nostarch.com').text
noStarchSoup = bs4.BeautifulSoup(res, 'html.parser')
print(noStarchSoup.prettify())