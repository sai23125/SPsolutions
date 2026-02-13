from flask import Flask, request, render_template, redirect, url_for
import csv
import os
from datetime import datetime

app = Flask(__name__)

# Folder & file setup
WAITLIST_FOLDER = "waitlist_data"
WAITLIST_FILE = os.path.join(WAITLIST_FOLDER, "waitlist.csv")

# Create folder if not exists
if not os.path.exists(WAITLIST_FOLDER):
    os.makedirs(WAITLIST_FOLDER)

# Create file with header if not exists
if not os.path.exists(WAITLIST_FILE):
    with open(WAITLIST_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Email", "Timestamp"])


# Homepage
@app.route("/")
def home():
    return render_template("index.html")


# Waitlist submission
@app.route("/waitlist", methods=["POST"])
def waitlist():
    email = request.form.get("email")

    if not email:
        return "Email required", 400

    with open(WAITLIST_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([email, datetime.now()])

    return redirect(url_for("thankyou"))


# Thank You page
@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")


if __name__ == "__main__":
    app.run()
