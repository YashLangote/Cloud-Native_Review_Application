from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

customers = []
reviews = []

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/review', methods=['POST'])
def add_review():
    data = request.get_json()
    if not data or 'product_id' not in data or 'text' not in data:
        return jsonify({"error": "Invalid data"}), 400

    review = {
        "product_id": data['product_id'],
        "text": data['text'],
        "rating": data.get('rating', 5)
    }
    reviews.append(review)
    return jsonify({"message": "Review added!", "review": review}), 201

@app.route('/reviews', methods=['GET'])
def get_reviews():
    return jsonify(reviews), 200

# 4. Create a Customer
@app.route('/customer', methods=['POST'])
def add_customer():
    data = request.get_json()

    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Invalid data"}), 400

    customer = {
        "id": len(customers) + 1,  # Simple auto-incrementing ID
        "name": data['name'],
        "email": data['email']
    }
    customers.append(customer)
    return jsonify({"message": "Customer created", "customer": customer}), 201
