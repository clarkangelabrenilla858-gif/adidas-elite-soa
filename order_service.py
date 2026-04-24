from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
from database_logic import session, Order 

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/place_order', methods=['POST'])
def place_order():
    data = request.json
    product_name = data.get('name')

    try:
        # 1. Check Inventory (Port 5001)
        inv_res = requests.post('http://127.0.0.1:5001/update_inventory', json=data)
        
        if inv_res.status_code == 200:
            # 2. Process Payment (Port 5002)
            pay_res = requests.post('http://127.0.0.1:5002/process_payment', json=data)
            
            # 3. Save to Aiven Cloud
            new_order = Order(
                product_name=product_name,
                quantity=data.get('qty'),
                total_price=data.get('total')
            )
            session.add(new_order)
            session.commit() 
            
            return jsonify({"message": "Success! Order saved to Aiven Cloud."})
        
        return jsonify({"message": "Inventory check failed"}), 400
    except Exception as e:
        session.rollback()
        return jsonify({"message": f"System error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)