from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(
    app,
    resources={r"/*": {"origins": "*"}},
    methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)

PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Keyboard", "price": 79.99},
    {"id": 3, "name": "Monitor", "price": 249.99},
    {"id": 4, "name": "Mouse", "price": 29.99},
    {"id": 5, "name": "USB-C Hub", "price": 49.99},
]


@app.route("/products", methods=["GET", "OPTIONS"])
def get_products():
    if request.method == "OPTIONS":
        return "", 204

    return jsonify(PRODUCTS)


@app.get("/health")
def health():
    return jsonify({"status": "ok", "service": "products-service"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)