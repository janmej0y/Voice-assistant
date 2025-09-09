from flask import Flask, request, jsonify, render_template
from assistant.skills import handle_command   # your assistant logic
import os

app = Flask(__name__, static_folder="frontend", template_folder="frontend")

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    user_input = data.get("message", "")
    response = handle_command(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
