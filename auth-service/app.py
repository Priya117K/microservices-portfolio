from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(
    app,
    resources={r"/*": {"origins": "*"}},
    methods=["POST", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)

@app.route('/login', methods=['POST', 'OPTIONS'])
def login():
    if request.method == 'OPTIONS':
        return '', 200

    data = request.get_json() or {}
    if data.get('username') == 'admin' and data.get('password') == 'password':
        return jsonify({"token": "fake-jwt-token-xyz123", "status": "success"}), 200
    return jsonify({"error": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)