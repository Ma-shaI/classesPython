from flask import Flask, render_template, url_for, request
import random
app = Flask(__name__,static_url_path='/static')
menu = [{'name': 'Home', 'url': 'home'}, {'name': 'Blog', 'url': 'blog'}, {'name': 'About us', 'url': 'about'},
        {'name': 'Contact us', 'url': 'contact'}]

blog_posts = [
    {"about": 'Posted on startup', 'title': 'Step-by-step guide to choosing great font pairs', 'author': 'By James West  |  May 23, 2022 ', 'text': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident.', 'img':'', 'url': 'post_1'},
    {"about": 'Featured Post', 'title': 'Step-by-step guide to choosing great font pairs', 'author': 'By John Doe   l   May 23, 2022 ', 'text': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident.', 'url': 'post_2'},

    {"about": 'TECHNOLOGY', 'title': '8 Figma design systems you can download for free today', 'author': 'By John Doe   l   May 23, 2022 ', 'text': '', 'url': 'post_3'},
    {"about": 'ECONOMY', 'title': 'Font sizes in UI design: The complete guide to follow', 'author': 'By James West  |  May 23, 2022', 'text': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident.', 'url': 'post_4'},
]
random_int = random.randint(0, len(blog_posts)-1)

@app.route('/')
@app.route('/home')
def home():
    print(random_int)
    return render_template('index.html', title='Home', menu=menu, posts=blog_posts, rand_int=1)


@app.route('/blog')
def blog():
    print(random_int)
    return render_template('blog.html', title='Blog', menu=menu, posts=blog_posts, rand_int=2)


@app.route('/about')
def about():
    return render_template('about.html', title='About', menu=menu)


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact', menu=menu)

@app.route('/privacy_policy')
def privacy_policy():
    return render_template('privacy_policy.html', title='Privacy Psolicy', menu=menu)
if __name__ == '__main__':
    app.run(debug=True)

