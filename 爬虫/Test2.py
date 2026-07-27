import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
ua=UserAgent()
Target_url="https://movie.douban.com/chart"
headers={"User-Agent":ua.random,
         "Referer":"https://www.douban.com/"}
response=requests.get(Target_url,headers=headers)
soup=BeautifulSoup(response.content,"html.parser")
for item in soup.find_all("tr",{"class":"item"}):
    title=item.find("div",{"class":"pl2"}).text
    print(title)
