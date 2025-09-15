from flask import Flask, render_template, request, jsonify
from assistant.skills import process_command  # Import your assistant logic

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_cmd = data.get("command", "")
    response = process_command(user_cmd)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
