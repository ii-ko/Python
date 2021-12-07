from flask import render_template
from flaskblog import app

posts = [{
    'author': 'ii-ko',
    'title': 'programming',
    'content': 'Python programming',
    'date_posted': 'May 3rd, 2012'
},
{
    'author': 'tamae',
    'title': 'design',
    'content': 'Web design',
    'date_posted': 'May 4th, 2012'
},
]


@app.route('/')
def index():
    return render_template('index.html', posts=posts, title='Home')


@app.route('/about')
def about():
    return render_template('about.html', title='About')