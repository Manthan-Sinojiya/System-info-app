from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message": "Hello from Demo DevOps App!"})

@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json() or {}
    return jsonify({"you_sent": data}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
