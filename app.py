from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message": "Hello from Demo DevOps App!"})

@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json() or {}
    return jsonify({"Hello 👋": data}), 201

# New feature in feature branch
@app.route("/status")
def status():
    return jsonify({
        "status": "ok",
        "version": "0.1.0",
        "environment": "development"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
