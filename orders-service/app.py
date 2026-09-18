from flask import Flask, jsonify

app = Flask(__name__)

ORDERS = [
    {"id": 1, "product_id": 1, "quantity": 1, "status": "confirmed"},
]


@app.get("/orders")
def get_orders():
    return jsonify(ORDERS)


@app.get("/health")
def health():
    return jsonify({"status": "ok", "service": "orders-service"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
