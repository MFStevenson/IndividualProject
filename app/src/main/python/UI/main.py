from flask import Flask, render_template, request, flash
from flask.helpers import url_for
from markupsafe import Markup
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

exp_design = {'data_file': None, "significance": None, 'iv': None, 'dv': None}

@app.route('/', methods = ['GET', 'POST'])
def index():
    if exp_design['data_file'] is None:
        # default value for no file uploaded
        return render_template('index.html', data_file = "No file, please choose a file to upload")
    return render_template('index.html', data_file = exp_design['data_file'])

# file operations, check that file is selected before carrying out action of upload or deletion
@app.route("/upload", methods = ['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['experimental_data']
        if file.filename == '':
            flash(Markup('<strong> Error:</strong> No file selected, please choose a file to upload'))
            return redirect(url_for('index'))

        filename = secure_filename(file.filename)
        exp_design['data_file'] = filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('File upload successful')
        return redirect(url_for('index'))
    else:
        flash('File not uploaded. Please try again')
        return redirect(url_for('index'))

@app.route("/del_file", methods = ["POST"])
def del_file():
    # check if there is actually a file to delete, if there is no file just return index, 
    # ensures that pressing this button will have no action if pressed by accident
    if exp_design['data_file'] is None:
        flash('No file to delete')
        return redirect(url_for('index'))
    # find file and delete, also need to notify the user of this happening
    filename = exp_design['data_file']
    exp_design['data_file'] = None
    cur_file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    os.remove(cur_file)
    flash('File deleted')
    return redirect(url_for('index'))

def design():
    d = read_exp_design()
    exp_design['significance'] = d['significance']
    exp_design['iv'] = d['iv'].lower().replace(" ", "")
    exp_design['dv'] = d['dv'].lower().replace(" ", "")

def run_stats():
    # generates the report, need to run the analysis to get the stats and visualisation
    # also get the p-val from inferential stats to compare against the level given by user
    result = run_analysis(exp_design)
    p_val = get_p()
    if p_val < exp_design["significance"]:
        s = True
    else:
        s = False

    return {"result": result["stats"], "vis": result["vis"], "s": s}

@app.route('/create_report', methods = ["GET", "POST"])
def create_report():
    # checking that experimental data exists, first we check for file, if no file then error given
    if request.method == "POST":
        if exp_design['data_file'] is None:
            flash(Markup('<strong>Error:</strong> No experimental data, please upload file'))
            return redirect(url_for('index'))

        design()

        # check that experimental design exists, if either iv or dv not given then error thrown
        if len(exp_design['iv']) == 0 or len(exp_design['dv']) == 0:
            flash(Markup('<strong>Error:</strong> Variables missing, please input variables and try again'))
            return redirect(url_for('index'))
            
        return render_template('create-report.html')
    else:
        return render_template('create-report.html')

# generate final report
@app.route('/report', methods = ['GET', 'POST'])
def report():
    if request.method == "POST":
        res = run_stats()
        return render_template('report.html', stats=res['result'], vis = res["vis"], significant = res['s'])
    else:
        # if no report is present, just send empty values
        return render_template('report.html', stats = {}, vis = None, significant = None)


if __name__ == "__main__":
    app.run()