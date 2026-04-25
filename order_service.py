from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app) # CRITICAL: This allows GitHub Pages to talk to Render

def get_db_connection():
    # Make sure this matches your actual .sql filename
    conn = sqlite3.connect('adidas_shop.db') 
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/place_order', methods=['POST'])
def place_order():
    data = request.json
    # Validate that we received the data
    if not data or 'name' not in data:
        return jsonify({"message": "Invalid order data"}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Ensure the 'orders' table exists before inserting
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name TEXT,
                quantity INTEGER,
                total_price REAL
            )
        ''')

        cursor.execute(
            "INSERT INTO orders (product_name, quantity, total_price) VALUES (?, ?, ?)",
            (data['name'], data['qty'], data['total'])
        )
        
        conn.commit()
        conn.close()
        return jsonify({"message": "Order saved to database!"}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)