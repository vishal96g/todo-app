from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB (local or Atlas)
client = MongoClient("mongodb://localhost:27017/")
db = client["todo_db"]
collection = db["items"]

@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    item_name = request.form.get("itemName")
    item_description = request.form.get("itemDescription")

    if not item_name or not item_description:
        return jsonify({"error": "Missing fields"}), 400

    collection.insert_one({
        "itemName": item_name,
        "itemDescription": item_description
    })

    return jsonify({"message": "Item stored successfully!"})

if __name__ == "__main__":
    app.run(debug=True)

