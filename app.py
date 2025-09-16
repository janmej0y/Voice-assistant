from flask import Flask, render_template, request, jsonify
from assistant.skills import process_command  # Import your assistant logic

from flask import Flask, render_template, request, jsonify, session
from assistant.skills import open_website

app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/command", methods=["POST"])
def command():
    data = request.get_json()
    cmd = data.get("command", "")

    response = open_website(cmd)  # response is now a dict
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
