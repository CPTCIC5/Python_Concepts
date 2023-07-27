import requests

def fetch_and_save_file(url,path):
    r=requests.get(url)
    with open(path,"w",encoding="utf-8") as f:
        f.write(r.text)

url = "https://timesofindia.indiatimes.com/city/delhi"
fetch_and_save_file(url,'times.html')