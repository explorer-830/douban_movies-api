from fastapi import FastAPI
import pymysql

app = FastAPI()
@app.get("/movies")
def get_movies():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="2004830",
        database="douban_movies",
        charset="utf8mb4"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT title, rating, people FROM movies LIMIT 50")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return {"data": [{"title": row[0], "rating": row[1], "people": row[2]} for row in rows]}