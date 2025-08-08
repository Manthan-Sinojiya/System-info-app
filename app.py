from flask import Flask, jsonify, request
import time

app = Flask(__name__)

# Track app start time
start_time = time.time()

@app.route("/")
def index():
    return jsonify({"message": "Hello from Demo DevOps App!"})

@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json() or {}
    return jsonify({"Welcome to Demo DevOps App": data}), 201

# Updated feature in dev branch
@app.route("/status")
def status():
    uptime_seconds = int(time.time() - start_time)
    return jsonify({
        "status": "ok",
        "version": "0.1.1",
        "environment": "development",
        "uptime_seconds": uptime_seconds
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
