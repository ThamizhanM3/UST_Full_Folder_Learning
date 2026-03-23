from flask import Flask, request, jsonify
import os
import pymysql

app = Flask(__name__)

DB_HOST = os.getenv("MYSQL_HOST", "db")
DB_PORT = int(os.getenv("MYSQL_PORT", "3306"))
DB_NAME = os.getenv("MYSQL_DATABASE", "appdb")
DB_USER = os.getenv("MYSQL_USER", "appuser")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD", "apppassword")

def get_conn():
    return pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.Cursor,
        autocommit=True,
    )

def init():
    conn = get_conn()
    with conn.cursor() as c:
        c.execute("CREATE TABLE IF NOT EXISTS notification (name VARCHAR(255))")
    conn.close()

@app.route("/items", methods=["GET"])
def get_items():
    conn = get_conn()
    with conn.cursor() as c:
        c.execute("SELECT name FROM notification")
        rows = c.fetchall()
    conn.close()
    return jsonify([r[0] for r in rows])

@app.route("/items", methods=["POST"])
def add_item():
    data = request.get_json(force=True)
    if not data or "name" not in data:
        return jsonify({"error": "name is required"}), 400

    conn = get_conn()
    with conn.cursor() as c:
        c.execute("INSERT INTO notification (name) VALUES (%s)", (data["name"],))
    conn.close()
    return {"status": "added"}

if __name__ == "__main__":
    init()
    app.run(host="0.0.0.0", port=5007)
