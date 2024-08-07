from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('messages.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()
    if request.method == 'POST':
        message = request.form['message']
        if message:
            conn.execute('INSERT INTO messages (content) VALUES (?)', (message,))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    messages = conn.execute('SELECT * FROM messages').fetchall()
    conn.close()
    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
