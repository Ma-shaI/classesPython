import random
import sqlite3
import os
from flask import Flask, render_template, url_for, request, session, redirect, abort, g
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
        db.close


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


blog_posts = [
    {"about": 'Posted on startup', 'title': 'Step-by-step guide to choosing great font pairs',
     'author': 'By James West  |  May 23, 2022 ',
     'text': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident.',
     'img': '', 'url': 'post_1'},
    {"about": 'Featured Post', 'title': 'Step-by-step guide to choosing great font pairs',
     'author': 'By John Doe   l   May 23, 2022 ',
     'text': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident.',
     'url': 'post_2'},

    {"about": 'TECHNOLOGY', 'title': '8 Figma design systems you can download for free today',
     'author': 'By John Doe   l   May 23, 2022 ', 'text': '', 'url': 'post_3'},
    {"about": 'ECONOMY', 'title': 'Font sizes in UI design: The complete guide to follow',
     'author': 'By James West  |  May 23, 2022',
     'text': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident.',
     'url': 'post_4'},
]
random_int = random.randint(0, len(blog_posts) - 1)


@app.route('/')
@app.route('/home')
def home():
    db = get_db()
    menu = FDataBase(db)
    return render_template('index.html', title='Home', menu=menu.get_menu(), posts=blog_posts, rand_int=1)


@app.route('/blog')
def blog():
    db = get_db()
    menu = FDataBase(db)
    return render_template('blog.html', title='Blog', menu=menu.get_menu(), posts=blog_posts, rand_int=2)


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


if __name__ == '__main__':
    app.run(debug=True)
