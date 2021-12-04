from flask import render_template
from flaskblog import app
from flaskblog.models.forms import RegistrationForm, LoginForm

posts = [{
    'author': 'Ihsan',
    'title': 'First post',
    'content': 'First content',
    'date_posted': 'May 3rd, 2012'
    },
    {
        'author': 'Ahmad',
        'title': 'Second post',
        'content': 'Second content',
        'date_posted': 'May 3rd, 2012'
    }
]


@app.route('/')
def home():
    return render_template('pages/index.html', posts=posts)


@app.route('/about')
def about():
    return render_template('pages/about.html')


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('auth/login.html', form=form)