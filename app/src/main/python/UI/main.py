from flask import Flask, render_template, request
from flask.helpers import url_for
from werkzeug.utils import redirect, secure_filename

import os

app = Flask(__name__)
app.config['DEBUG'] = True

#dirs, should be in settings.py
UPLOAD_FOLDER = '/experimental_data/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# views.py (urls for html pages)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_report')
def generate_report():
    return render_template('generate_report.html')

@app.route('/edit_report')
def edit_report():
    return render_template('edit_report.html')

@app.route('/report')
def report():
    return render_template('report.html')

#file_management.py
@app.route("/upload_data", methods = ["GET", "POST"])
def upload():
    if request.method == 'POST':
        file = request.files['experimental_data']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
        return 0
    else:
        return 1

if __name__ == "__main__":
    app.run()