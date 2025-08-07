from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

GOALS_FILE = "goals.json"

# Tải dữ liệu từ file goals.json
def load_goals():
    if os.path.exists(GOALS_FILE):
        with open(GOALS_FILE, "r") as f:
            return json.load(f)
    return []

# Lưu dữ liệu vào file goals.json
def save_goals(goals):
    with open(GOALS_FILE, "w") as f:
        json.dump(goals, f)

# Danh sách mục tiêu
goals = load_goals()

@app.route("/")
def index():
    return render_template("index.html", goals=goals)

@app.route("/add", methods=["POST"])
def add_goal():
    name = request.form.get("name")
    due_date = request.form.get("due_date")
    if name:
        goal = {
            "name": name,
            "due_date": due_date,
            "status": False  # mặc định là chưa làm
        }
        goals.append(goal)
        save_goals(goals)
    return redirect("/")

@app.route("/toggle/<int:index>", methods=["POST"])
def toggle_status(index):
    if 0 <= index < len(goals):
        goals[index]["status"] = not goals[index]["status"]
        save_goals(goals)
    return redirect("/")

@app.route("/delete/<int:index>", methods=["POST"])
def delete_goal(index):
    if 0 <= index < len(goals):
        goals.pop(index)
        save_goals(goals)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10000)
