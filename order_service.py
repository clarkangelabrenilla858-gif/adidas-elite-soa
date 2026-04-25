from flask import Flask, request, jsonify
from flask_cors import CORS
# Import the cloud session and Order model from your other file
from database_logic import session, Order 

app = Flask(__name__)
CORS(app)

@app.route('/place_order', methods=['POST'])
def place_order():
    data = request.json
    if not data or 'name' not in data:
        return jsonify({"message": "Invalid order data"}), 400

    try:
        # Create a new Order object using the Aiven Cloud model
        new_order = Order(
            product_name=data['name'],
            quantity=data['qty'],
            total_price=data['total']
        )
        
        # Add and COMMIT to the cloud database
        session.add(new_order)
        session.commit() 
        
        print(f"Order #20+ saved to Aiven: {data['name']}")
        return jsonify({"message": "Order saved to Aiven Cloud!"}), 200
        
    except Exception as e:
        session.rollback() # Undo if it fails
        print(f"Error: {e}")
        return jsonify({"message": str(e)}), 500

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)