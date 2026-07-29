# 豆瓣电影数据采集与查询系统

## 项目简介

本项目基于 Python 开发，实现了从豆瓣电影新片榜采集电影数据，并将数据存储到 MySQL 数据库中，最后使用 FastAPI 提供 REST API 查询接口。

通过本项目熟悉了 Python 爬虫、HTML 解析、数据库操作以及 Web API 开发的完整流程。

---

## 技术栈

- Python
- Requests
- BeautifulSoup4
- PyMySQL
- MySQL
- FastAPI

---

## 项目功能

### 1. 爬取豆瓣电影数据

使用 Requests 向豆瓣电影发送 HTTP 请求。

```python
requests.get(url, headers=headers)
```

---

### 2. 解析网页

使用 BeautifulSoup 解析 HTML 页面，提取：

- 电影名称
- 电影评分
- 评价人数
- 电影链接

---

### 3. 数据库存储

使用 PyMySQL 将电影信息存入 MySQL。

数据库表结构如下：

| 字段 | 类型 |
|------|------|
| id | INT |
| title | VARCHAR(100) |
| rating | VARCHAR(10) |
| people | VARCHAR(50) |
| url | VARCHAR(200) |

---

### 4. 提供 REST API

使用 FastAPI 编写接口：

```
GET /movies
```

返回 JSON 数据：

```json
{
    "data":[
        {
            "title":"哪吒2",
            "rating":"9.2",
            "people":"120万人评价"
        }
    ]
}
```

---

## 项目流程

```
豆瓣电影

↓

Requests 请求网页

↓

BeautifulSoup 解析 HTML

↓

MySQL 存储电影数据

↓

FastAPI 提供查询接口

↓

JSON 返回数据
```

---

## 项目运行

### 安装依赖

```bash
pip install fastapi
pip install pymysql
pip install requests
pip install beautifulsoup4
pip install uvicorn
```

---

### 创建数据库

运行：

```
Mysql.py
```

程序将：

- 创建数据库
- 创建 movies 表
- 爬取豆瓣电影数据
- 保存到 MySQL

---

### 启动 FastAPI

```bash
uvicorn main:app --reload
```

浏览器访问：

```
http://127.0.0.1:8000/docs
```

即可查看 Swagger API 文档。

---

## 项目收获

通过本项目掌握了：

- Python 网络请求
- BeautifulSoup HTML 解析
- MySQL 数据库操作
- FastAPI Web API 开发
- RESTful API 基础设计
- JSON 数据返回
