from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(
    app,
    resources={r"/*": {"origins": "*"}},
    methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)

ORDERS = [
    {"id": 101, "product_id": 1, "quantity": 1, "status": "confirmed"},
    {"id": 102, "product_id": 2, "quantity": 2, "status": "processing"},
]


@app.route("/orders", methods=["GET", "POST", "OPTIONS"])
def get_orders():
    if request.method == "OPTIONS":
        return "", 204

    if request.method == "POST":
        data = request.get_json() or {}
        order = {
            "id": data.get("id", max(order["id"] for order in ORDERS) + 1),
            "product_id": data.get("product_id"),
            "quantity": data.get("quantity", 1),
            "status": data.get("status", "pending"),
        }
        ORDERS.insert(0, order)
        return jsonify(order), 201

    return jsonify(ORDERS)


@app.get("/health")
def health():
    return jsonify({"status": "ok", "service": "orders-service"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
