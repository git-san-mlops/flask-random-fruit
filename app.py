from flask import Flask, jsonify
import random

app = Flask(__name__)

fruits = ["apple", "banana", "mango", "orange", "grape"]

@app.route("/")
def home():
    return jsonify({"message": "Fruit Service Running "})

@app.route("/random-fruit")
def random_fruit():
    return jsonify({"fruit": random.choice(fruits)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)