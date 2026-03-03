from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Holymary2005**",
        database="icoms"
    )

# --- API ROUTES ---

@app.route('/api/users', methods=['GET'])
def get_users():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT id, name, role FROM users")
    users = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify(users)

@app.route('/api/users', methods=['POST'])
def add_user():
    data = request.json
    db = get_db()
    cursor = db.cursor()
    query = "INSERT INTO users (name, role) VALUES (%s, %s)"
    cursor.execute(query, (data['name'], data['role']))
    db.commit()
    new_id = cursor.lastrowid
    cursor.close()
    db.close()
    return jsonify({"id": new_id, "message": "User added successfully"})

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    db.commit()
    cursor.close()
    db.close()
    return jsonify({"message": "User deleted"})

# ... keep your existing @app.route definitions below ...
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
    # Note: Your login script redirects to 'client-tracking.html'
    return render_template('client.html')

@app.route('/users.html')
def users():
    return render_template('users.html')

if __name__ == '__main__':
    app.run(debug=True)