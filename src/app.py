import os
import psycopg2
from flask import Flask, request, jsonify
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(os.getenv('DATABASE_URL'))
    return conn

# --- User Endpoints ---

@app.route('/login-full', methods=['POST'])
def login_full():
    data = request.json
    user_id = data.get('user')
    password = data.get('psw')
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT name, role FROM users WHERE id = %s AND password = %s', (user_id, password))
    user = cur.fetchone()
    cur.close()
    conn.close()

    if user:
        return jsonify({"status": 1, "name": user[0], "role": user[1]})
    return jsonify({"status": 0})

@app.route('/login-status', methods=['POST'])
def login_status():
    data = request.json
    user_id = data.get('user')
    password = data.get('psw')
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT 1 FROM users WHERE id = %s AND password = %s', (user_id, password))
    exists = cur.fetchone()
    cur.close()
    conn.close()

    return jsonify({"status": 1 if exists else 0})

# --- Attendance Endpoints ---

@app.route('/attendance', methods=['POST'])
def add_attendance():
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO attendance_records (user_id, log_type, log_time) VALUES (%s, %s, %s)',
        (data['user_id'], data['log_type'], data['log_time'])
    )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "Record added successfully"}), 201

@app.route('/attendance/<user_id>/<period>', methods=['GET'])
def get_attendance(user_id, period):
    """
    period can be: 'day', 'week', 'month'
    Expects a query param ?date=YYYY-MM-DD
    """
    target_date = request.args.get('date', datetime.now().strftime('%Y-%m-%d'))
    
    query_map = {
        'day': "log_time::date = %s",
        'week': "date_trunc('week', log_time) = date_trunc('week', %s::date)",
        'month': "date_trunc('month', log_time) = date_trunc('month', %s::date)"
    }

    if period not in query_map:
        return jsonify({"error": "Invalid period"}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    query = f"SELECT id, log_type, log_time FROM attendance_records WHERE user_id = %s AND {query_map[period]}"
    cur.execute(query, (user_id, target_date))
    rows = cur.fetchall()
    cur.close()
    conn.close()

    results = [{"id": r[0], "log_type": r[1], "log_time": r[2].isoformat()} for r in rows]
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)