from flask import Flask, render_template, request, redirect, url_for
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Danh sách mục tiêu lưu tạm trong bộ nhớ
goals = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        goal_text = request.form.get("goal")
        status = request.form.get("status")
        deadline = request.form.get("deadline")
        if goal_text and status and deadline:
            goals.append({
                "goal": goal_text,
                "status": status,
                "deadline": deadline
            })
        return redirect(url_for("index"))
    return render_template("index.html", goals=goals)

if __name__ == "__main__":
    app.run(debug=True)
