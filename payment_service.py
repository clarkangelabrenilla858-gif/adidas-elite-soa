from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/process_payment', methods=['POST'])
def process_payment():
    # Simulated payment success logic
    return jsonify({"Status": "Success"})

if __name__ == '__main__':
    app.run(port=5002, debug=True)