from flask import Flask, render_template, request, flash
from flask.helpers import url_for
from werkzeug.utils import redirect, secure_filename
import os

from Backend.data_processing import *

app = Flask(__name__)
app.config['DEBUG'] = True
app.config["SECRET_KEY"] = os.urandom(24)
app.config['TEMPLATES_AUTO_RELOAD'] = True

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_ROOT = 'Backend/experimental_data/'
UPLOAD_FOLDER = os.path.join(BASE_DIR, UPLOAD_ROOT)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/upload", methods = ['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['experimental_data']
        if file.filename == '':
            return redirect(url_for('index'))

        filename = secure_filename(file.filename)
        global exp_design
        exp_design = {}
        exp_design['data_file'] = filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('File upload successful')
        return redirect(url_for('index'))
    else:
        flash('File not uploaded. Please try again', 'error')
        return redirect(url_for('index'))

def design():
    d = read_exp_design() 
    exp_design['significance'] = d['significance']
    exp_design['iv'] = d['iv'].lower().replace(" ", "")
    exp_design['dv'] = d['dv'].lower().replace(" ", "")

def run_stats():
    # need to get this from previous function
    result= run_analysis(exp_design)
    p_val = get_p()
    if p_val < exp_design["significance"]:
        s = True
    else:
        s = False

    return {"result": result["stats"], "vis": result["vis"], "s": s}

@app.route('/create_report', methods = ["GET", "POST"])
def create_report():
    if request.method == "POST":
        design()
        return render_template('create-report.html')
    else:
        return render_template('create-report.html')

@app.route('/report', methods = ['GET', 'POST'])
def report():
    if request.method == "POST":
        res = run_stats()
        return render_template('report.html', stats=res['result'], vis = res["vis"], significant = res['s'])
    else:
        return render_template('report.html', stats = {}, vis = None, significant = None)

@app.route('/save_pdf', methods = ['GET', 'POST'])
def save_pdf():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()