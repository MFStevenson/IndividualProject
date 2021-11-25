from flask import url_for

@app.route('/static/')
def static():
    return 'static'