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
@app.route("/experimental_data", methods = ["GET", "POST"])
def upload():
    if request.method == 'POST':
        file = request.files['experimental_data']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'file uploaded'
    else:
        return 'error: file was not uploaded'

if __name__ == "__main__":
    app.run()