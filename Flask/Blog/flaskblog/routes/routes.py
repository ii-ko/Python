from flask import render_template, flash, redirect, url_for
from flaskblog import app, bcrypt, db
from flaskblog.models.forms import RegistrationForm, LoginForm
from flaskblog.models.database import Users

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


# register new account
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        data = Users(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(data)
        db.session.commit()
        flash(f'Your account has been created. You are now able to log in.', 'success')
        return redirect(url_for('login'))
    return render_template('auth/register.html', form=form)