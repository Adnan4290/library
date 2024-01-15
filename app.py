# app.py
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    subjects = ['CIT-303', 'CIT-333', 'CIT-344', 'CIT-352']  # Updated with CIT-352
    return render_template('index.html', subjects=subjects)

@app.route('/notes/<subject>/<filename>')
def get_note(subject, filename):
    return send_from_directory(f'notes/{subject}', filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


