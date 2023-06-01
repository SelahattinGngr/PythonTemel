import requests
from bs4 import BeautifulSoup


url ="https://www.trendyol.com/sr?q=diz%C3%BCst%C3%BC%20bilgisayar&qt=diz%C3%BCst%C3%BC%20bilgisayar&st=diz%C3%BCst%C3%BC%20bilgisayar&os=1"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

list =soup.find_all("div",{"class":"prdct-cntnr-wrppr"},limit=1)


for div in list:
    title = div.find("span",{"class":"prdct-desc-cntnr-name hasRatings"}).text
    link= div.a.get("href")
    price=div.find("div",{"class":"prc-box-dscntd"}).text
    print(title,link,price)

