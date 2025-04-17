import os
import pickle
import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()

    if user:
        return "Login successful"
    else:
        return "Login failed"

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save('/tmp/' + file.filename)  # 경로 검증 없음
    return "File uploaded"

@app.route('/deserialize', methods=['POST'])
def deserialize():
    data = request.data
    obj = pickle.loads(data)
    return f"Received object: {obj}"

@app.route('/execute', methods=['POST'])
def execute():
    cmd = request.form['cmd']
    os.system(cmd)
    return "Command executed"
