from flask import Flask, render_template, request
from flask.helpers import url_for
from werkzeug.utils import redirect

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html')

# issue with template, cannot build url_for endpoint error - need to sort this to link everything together
@app.route('/UI/templates/<string>:template')
def templates(template):
    return render_template(template)

@app.route("/upload-data", methods = ["GET", "POST"])
def upload():
    if request.method == 'POST':
        file = request.files['experimental_data']
    
    return 0

if __name__ == "__main__":
    app.run()