import sqlite3
import os
import datetime
from flask import Flask, render_template, url_for, request, flash, session, redirect, abort, g
from FDataBase import FDataBase

DATABASE = '/tmp/flsk.db'
DEBAG = True
SECRET_KEY = 'baea1a026fe22154488588f7945d531c53efddb7'
app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(DATABASE=os.path.join(app.root_path, 'flsk.db'))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', 'r') as f:
        db.cursor().executescript(f.read())
        db.commit()
        db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db



@app.route('/')
@app.route('/home')
def home():
    db = get_db()
    menu = FDataBase(db)
    return render_template('index.html', title='Home', menu=menu.get_menu(), post=menu.get_post(2))


@app.route('/blog')
def blog():
    db = get_db()
    menu = FDataBase(db)
    return render_template('blog.html', title='Blog', menu=menu.get_menu(), post=menu.get_post(1),
                           posts=menu.get_all_posts())


@app.route('/about')
def about():
    db = get_db()
    menu = FDataBase(db)
    return render_template('about.html', title='About', menu=menu.get_menu())


@app.route('/contact')
def contact():
    db = get_db()
    menu = FDataBase(db)
    return render_template('contact.html', title='Contact', menu=menu.get_menu())


@app.route('/privacy_policy')
def privacy_policy():
    db = get_db()
    menu = FDataBase(db)
    return render_template('privacy_policy.html', title='Privacy Psolicy', menu=menu.get_menu())


@app.route('/blog_post<int:id_post>')
def blog_post(id_post):
    db = get_db()
    data = FDataBase(db)
    time = data.get_post(id_post)[-2]
    s_datetime = datetime.datetime.fromtimestamp(time)
    times = s_datetime.strftime('%Y-%m-%d')
    return render_template('blog_post.html', title='Blog Post', menu=data.get_menu(), blog_post=data.get_post(id_post), time=times)

@app.route('/<username>')
def profile(username):
    db = get_db()
    data = FDataBase(db)
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    else:
        data.add_author(username)
        return render_template('profile.html', title=username,menu=data.get_menu(), my_posts=data.get_my_post(username))


@app.route('/login', methods=['POST', 'GET'])
def login():
    db = get_db()
    data = FDataBase(db)
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == 'Mary' and request.form['psw'] == '123456':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
    return render_template('login.html', title='Авторизация', menu=data.get_menu())

@app.route('/add_post', methods=['POST', 'GET'])
def add_post():
    db = get_db()
    data = FDataBase(db)
    username=session['userLogged']
    if request.method == 'POST':
        if len(request.form['title']) > 4 and len(request.form['text']) > 40 and len(request.form['short_text'])>10:
            res = data.add_post(request.form['title'],request.form['category_title'], username, request.form['short_text'], request.form['text'])
            if not res:
                flash("Ошибка добавления статьи", category='error')
            else:
                flash('Статья добавлена успешно', category='success')
        else:
            flash("Ошибка добавления статьи", category='error')
    return render_template('add_post.html', title='Blog Post', menu=data.get_menu())


if __name__ == '__main__':
    app.run(debug=True)
