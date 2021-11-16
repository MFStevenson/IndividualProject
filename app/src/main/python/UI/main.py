from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/upload-data", methods = ["GET", "POST"])
def upload():

    return 0
    
if __name__ == "__main__":
    app.run()