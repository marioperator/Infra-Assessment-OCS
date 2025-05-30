from flask import Flask, render_template, request, redirect, url_for, session, send_file
import os
from functools import wraps

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "changeme")

USERS = {"admin": "changeme"}
LOG_FILE = "report_generation.log"

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form.get("username")
        pw = request.form.get("password")
        if USERS.get(user) == pw:
            session["user"] = user
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Credenziali errate")
    return render_template("login.html")

@app.route("/")
@login_required
def dashboard():
    with open(LOG_FILE, "r") as f:
        logs = f.readlines()
    return render_template("dashboard.html", logs=logs)

@app.route("/generate-report")
@login_required
def generate_report():
    os.system("python3 ../report-worker/app.py")
    with open(LOG_FILE, "a") as f:
        f.write(f"{session['user']} ha generato report\n")
    return redirect(url_for("dashboard"))

@app.route("/download")
@login_required
def download_report():
    filename = "../report-worker/Assessment_Infrastrutturale_IT.docx"
    return send_file(filename, as_attachment=True)

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    if not os.path.exists(LOG_FILE):
        open(LOG_FILE, "w").close()
    app.run(host="0.0.0.0", port=5001, debug=True)
