from flask import Flask
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        database=os.getenv("DB_NAME", "testdb"),
        user=os.getenv("DB_USER", "admin"),
        password=os.getenv("DB_PASSWORD", "admin")
    )

    return conn

@app.route("/")
def home():
    conn = get_db_connection()
    cur =  conn.cursor()
    cur.execute("SELECT 1")
    result = cur.fetchall()
    cur.close()
    conn.close()
    return f"DB connected: {result}"


if __name__ == "__main__":
    app.run(host="0.0.0.0",port = 5000)