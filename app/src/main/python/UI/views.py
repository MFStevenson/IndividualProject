# maybe move code from main to this file, need to look up flask documentation in more detail
# to get a bette idea of how to structure my directory and what code should go in what file
# look at jinja for templates

from flask import Flask, render_template, request
from flask.helpers import url_for
from werkzeug.utils import redirect

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/upload_data", methods = ["GET", "POST"])
def upload():
    if request.method == 'POST':
        file = request.files['experimental_data']
    
    return 0

@app.route('/generate_report')
def generate_report():
    return render_template('generate_report.html')

@app.route('/edit_report')
def edit_report():
    return render_template('edit_report.html')

@app.route('/report')
def report():
    return render_template('report.html')