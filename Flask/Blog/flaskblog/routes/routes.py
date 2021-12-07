from flask import render_template
from flaskblog import app
from flaskblog.models.forms import RegistrationForm, LoginForm

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
    return render_template('pages/index.html', posts=posts, title='Home')


@app.route('/about')
def about():
    return render_template('pages/about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('auth/register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('auth/login.html', title='Login', form=form)