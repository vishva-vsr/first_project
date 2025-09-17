from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow React frontend to call API

@app.route("/api/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello from Python backend!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
