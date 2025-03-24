from flask import Flask, request, jsonify

app = Flask(__name__)

VERIFY_TOKEN = "MySecret123"

@app.route("/", methods=["GET"])
def verify():
    token_sent = request.args.get("hub.verify_token")
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "Invalid token", 403

@app.route("/", methods=["POST"])
def receive_message():
    data = request.get_json()
    print("Incoming message:", data)
    return jsonify({"status": "received"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
