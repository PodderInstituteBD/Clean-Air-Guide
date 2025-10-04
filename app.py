from flask import Flask, jsonify
import requests
import json

app = Flask(_name_)

NASA_API_KEY = "DEMO_KEY"  # এখানে চাইলে আপনার API key বসাতে পারেন
API_URL = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"

def get_nasa_data():
    try:
        print("🌍 Fetching NASA data online...")
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()
        data = response.json()
        print("✅ NASA data loaded from API.")
    except Exception as e:
        print(f"⚠️ NASA API not available ({e}). Using local backup data instead.")
        with open("data.json", "r") as file:
            data = json.load(file)
    return data

@app.route("/")
def home():
    return "🚀 NASA Flask API is running!"

@app.route("/nasa")
def nasa():
    data = get_nasa_data()
    return jsonify(data)   # JSON format এ ব্রাউজারে দেখাবে

if _name_ == "_main_":
    app.run(debug=True)
