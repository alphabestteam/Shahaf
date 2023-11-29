import mysql.connector
from mysql.connector import Error
from flask import Flask
import os
from dotenv import load_dotenv
from flask import request, jsonify

app = Flask(__name__)

load_dotenv()

def connect():
    try:
        connection = mysql.connector.connect(host=os.getenv("MYSQL_HOST"),
                                            database=os.getenv("MYSQL_DB"),
                                            user=os.getenv("MYSQL_USER"),
                                            password=os.getenv("MYSQL_PASSWORD"),
                                            port=3306)
        if connection.is_connected():
            return connection

    except Error as error:
        print("Error while connecting to MySQL", error)

def add_db():
    connection = connect()
    with connection.cursor(dictionary=True) as cursor:
        cursor.execute(f"SHOW TABLES LIKE 'users'")
        is_table_exists = cursor.fetchone()

        if not is_table_exists:
            cursor.execute(f"CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")

@app.route("/<table>", methods = ["POST"])
def add(table: str):
    connection = connect()
    add_db()
    data = request.json
    try:
        name = data.get("name")
        query = f"INSERT INTO {table} (name) VALUES ('{name}')"
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute(query)
            connection.commit()
            id = cursor.lastrowid

        cursor.close()
        connection.close()
        print("MySQL connection is closed")
        return (f"User {name} was successfully added to the database with the id {id}")

    except Error as e:
        return jsonify({"error": f"Error: {e}"}), 500

@app.route("/<table>", methods = ["GET"])
def get(table: str):
    connection = connect()
    add_db()
    try:
        query = f"SELECT * FROM {table};"
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute(query)
            records = cursor.fetchall()

        cursor.close()
        connection.close()
        print("MySQL connection is closed")
        return jsonify(records)

    except Error as e:
        return jsonify({"error": f"Error: {e}"}), 500
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)