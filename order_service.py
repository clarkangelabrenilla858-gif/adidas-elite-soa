from flask import Flask, request, jsonify
from flask_cors import CORS
from database_logic import session, Order

app = Flask(__name__)
CORS(app)

@app.route('/place_order', methods=['POST'])
def place_order():
    data = request.json
    try:
        # Create a new row for the 'orders' table
        new_order = Order(
            product_name=str(data['name']),
            quantity=int(data['qty']),
            total_price=int(data['total'])
        )
        session.add(new_order)
        session.commit() # This is where the 'save' happens
        return jsonify({"message": "Success"}), 200
    except Exception as e:
        session.rollback() # Clears the error if it fails
        print(f"Detailed Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)