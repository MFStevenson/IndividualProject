from curses import flash
from flask import Flask, render_template, request, flash
from flask.helpers import url_for
from werkzeug.utils import redirect, secure_filename

import os

app = Flask(__name__)
app.config['DEBUG'] = True
app.config["SECRET_KEY"] = os.urandom(24)

#dirs, should be in settings.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_ROOT = 'experimental_data/'
UPLOAD_FOLDER = os.path.join(BASE_DIR, UPLOAD_ROOT)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# views.py (urls for html pages)
@app.route('/', methods = ['GET', 'POST'])
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
@app.route("/upload", methods = ['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['experimental_data']
        if file.filename == '':
            flash('No selected file')
            return redirect(url_for('index'))
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('index'))
    else:
        flash('Error: file was not uploaded')
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()