from flask import Flask, render_template, request, session
from main import process_command

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for session storage

@app.route("/", methods=["GET", "POST"])
def index():
    if "chat" not in session:
        session["chat"] = []

    if request.method == "POST":
        cmd = request.form["command"]
        response = process_command(cmd)

        # Save user input & assistant response
        session["chat"].append(("You", cmd))
        session["chat"].append(("Assistant", response))

    return render_template("index.html", chat=session["chat"])

if __name__ == "__main__":
    app.run(debug=True)
