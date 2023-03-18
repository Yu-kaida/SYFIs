from scr import app
from flask import render_template, request

@app.route('/')
def index():
    data = {
        'listing':['enjoy sharing','Have a nice day!','Goody!']
    }
    return render_template('syfis/index.html',data=data)

@app.route('/test')
def other1():
    return 'This is test version'

@app.route('/form', methods=['GET','POST'])
def sample_form():
    if request.method == 'GET':
        return render_template('syfis/form.html')
    if request.method == 'POST':
        print('Form posted.')
    req1 = request.form['id']
    return f'Thank you, {req1}! Form posted.'
    