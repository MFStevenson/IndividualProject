from curses import flash
from distutils.log import error
from flask import Flask, render_template, request, flash
from flask.helpers import url_for
from werkzeug.utils import redirect, secure_filename
import os
import sys

from Backend.data_processing import *

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

@app.route('/create_report', methods = ["GET", "POST"])
def edit_report():
    if request.method == "POST":
        exp_design = design()
    return render_template('create_report.html')

@app.route('/report', methods = ['GET', 'POST'])
def report():
    #if request.method == "POST":
    return redirect(url_for("run_stats"))
    #else:
     #   flash("Error: Report Not Generated, please check that you have input everything")
      #  return render_template('edit_report.html')

def design():
        exp_design = read_exp_design()
        dvs = exp_design['dv']
        ivs = exp_design['iv']
        signififance = exp_design['significance']

        return render_template('create_report.html')

@app.route("/run_stats", methods = ["GET", "POST"])
def run_stats():
    # need to get this from previous function
    result = run_analysis(exp_design=design())
    return render_template('report.html', stats=result)

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