from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from pathlib import Path

app = Flask(__name__)
app.secret_key = 'change-this-secret-key'
DB_PATH = Path(__file__).with_name('learnbridge.db')

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db() as db:
        db.execute('''CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )''')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()
        if not all([name, email, message]):
            flash('Please complete every field.', 'error')
        else:
            with get_db() as db:
                db.execute('INSERT INTO messages (name, email, message) VALUES (?, ?, ?)', (name, email, message))
            flash('Thanks! Your message has been saved.', 'success')
            return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
