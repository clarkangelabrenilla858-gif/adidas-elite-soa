from flask import Flask, request, jsonify
from flask_cors import CORS
from database_logic import session, Product

app = Flask(__name__)
CORS(app)

@app.route('/get_inventory', methods=['GET'])
def get_inventory():
    shoes = session.query(Product).all()
    return jsonify([{"id": s.id, "name": s.name, "price": s.price, "img": s.img_path} for s in shoes])

# --- ADD OR FIX THIS ROUTE ---
@app.route('/update_inventory', methods=['POST'])
def update_inventory():
    data = request.json
    product_name = data.get('name')
    
    # Just checking if the shoe exists in our database
    shoe = session.query(Product).filter_by(name=product_name).first()
    
    if shoe:
        print(f"Inventory check passed for: {product_name}")
        return jsonify({"message": "Inventory confirmed"}), 200
    else:
        print(f"Inventory check failed: {product_name} not found")
        return jsonify({"message": "Product not found"}), 404

if __name__ == '__main__':
    import os
    # Render provides a 'PORT' environment variable. If it's not there, it uses 5001.
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port)