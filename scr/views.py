from scr import app
from flask import render_template

@app.route('/')
def index():
    data = {
        'listing':['enjoy sharing','Have a nice day!','Goody!']
    }
    return render_template('syfis/index.html',data=data)

@app.route('/test')
def other1():
    return 'This is test version'

@app.route('/form')
def sample_form():
    return render_template('syfis/form.html')