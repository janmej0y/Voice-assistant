from flask import Flask, render_template, request, jsonify
from assistant.skills import open_website

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/command", methods=["POST"])
def command():
    data = request.get_json()
    cmd = data.get("command", "")

    response = open_website(cmd)
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
