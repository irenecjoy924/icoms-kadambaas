from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Database connection pointing to your schema 'icoms'
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Holymary2005**",
        database="icoms"
    )

# --- USERS API ROUTES ---

@app.route('/api/users', methods=['GET'])
def get_users():
    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)
        # We fetch username (the person's name) and their category (role)
        cursor.execute("SELECT id, username, role FROM users")
        users = cursor.fetchall()
        cursor.close()
        db.close()
        return jsonify(users)
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@app.route('/api/users', methods=['POST'])
def add_user():
    try:
        data = request.get_json()
        db = get_db()
        cursor = db.cursor()
        # 'username' is the person's name (e.g., Sourab)
        # 'role' is the category (e.g., Dispatcher)
        query = "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)"
        cursor.execute(query, (data['name'], 'User@123', data['role']))
        db.commit()
        new_id = cursor.lastrowid
        cursor.close()
        db.close()
        return jsonify({"id": new_id, "message": "User added successfully"}), 201
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"message": str(e)}), 500

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        db.commit()
        cursor.close()
        db.close()
        return jsonify({"message": "User deleted"})
    except Exception as e:
        return jsonify({"message": str(e)}), 500

# --- PAGE NAVIGATION ---

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/admin.html')
def admin():
    return render_template('admin.html')

@app.route('/supervisor.html')
def supervisor():
    return render_template('supervisor.html')

@app.route('/orders.html')
def orders():
    return render_template('orders.html')

@app.route('/dispatcher.html')
def dispatcher():
    return render_template('dispatcher.html')

@app.route('/notifications.html')
def notifications():
    return render_template('notifications.html')

@app.route('/client-tracking.html')
def client():
    return render_template('client.html')

@app.route('/users.html')
def users():
    return render_template('users.html')

if __name__ == '__main__':
    app.run(debug=True)