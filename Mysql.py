import pymysql
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# 1. 连接 MySQL
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="2004830",  
    charset="utf8mb4"
)
cursor = conn.cursor()

# 2. 创建数据库
cursor.execute("CREATE DATABASE IF NOT EXISTS douban_movies")
conn.select_db("douban_movies")

# 3. 创建电影表
cursor.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(100),
        rating VARCHAR(10),
        people VARCHAR(50),
        url VARCHAR(200)
    )
""")

# 4. 爬取豆瓣新片榜
url = "https://movie.douban.com/chart"
ua=UserAgent()
headers = {"User-Agent": ua.random}
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, "html.parser")

# 5. 解析并存入数据库
for tr in soup.select("tr.item"):
    a_tag = tr.select_one(".pl2 a")
    if not a_tag:
        continue
    title = a_tag.text.strip().replace("\n", "").replace(" ", "")
    rating_tag = tr.select_one(".rating_nums")
    rating = rating_tag.text.strip() if rating_tag else "暂无"
    people_tag = tr.select_one(".pl")
    people = people_tag.text.strip() if people_tag else "暂无"
    url_tag = a_tag.get("href")

    cursor.execute("""
        INSERT INTO movies (title, rating, people, url)
        VALUES (%s, %s, %s, %s)
    """, (title, rating, people, url_tag))
    print(f" 已存入：{title} | {rating} | {people}")

# 6. 提交并关闭
conn.commit()
cursor.close()
conn.close()
print(" 所有数据已存入 MySQL！")
