from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dữ liệu mẫu lưu tạm trên RAM (chưa dùng CSDL)
goals = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_goal():
    title = request.form.get('title')
    description = request.form.get('description')
    if title:
        goals.append({
            'title': title,
            'description': description
        })
    return redirect(url_for('list_goals'))

@app.route('/list')
def list_goals():
    return render_template('list.html', goals=goals)

if __name__ == '__main__':
    app.run(debug=True)
