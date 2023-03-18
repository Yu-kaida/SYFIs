from scr import app
from flask import render_template, request, redirect, url_for
from scr import db
from scr.models.member_fav import Member

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
        form_name = request.form['name']
        form_id = request.form['id']
        form_fav1 = request.form['fav1']
        form_fav2 = request.form['fav2']
        form_fav3 = request.form['fav3']
        form_fav4 = request.form['fav4']
        form_fav5 = request.form['fav5']

        fav_member = Member(
            username=form_name, 
            id=form_id, 
            fav1=form_fav1, 
            fav2=form_fav2, 
            fav3=form_fav3, 
            fav4=form_fav4, 
            fav5=form_fav5
        )
        db.session.add(fav_member)
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/list')
def fav_list():
    fav_list = Member.query.all()
    return render_template('syfis/fav_list.html', fav_list=fav_list)