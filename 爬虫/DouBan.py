
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
ua=UserAgent()
headers = {"User-Agent":ua.random,
           "Referer":"https://www.douban.com/"}
Target_url="https://movie.douban.com/top250"
response=requests.get(Target_url,headers=headers)
print(response.text)
soup=BeautifulSoup(response.text,"html.parser")
for item in soup.find_all("div",class_="item"):
    title=item.find("span",class_="title").text
    rting=item.find("span",class_="rating_num").text
    print(f"电影{title}的评分是{rting}")