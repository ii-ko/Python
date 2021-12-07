from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user, logout_user
from flaskblog import app, db, bcrypt
from flaskblog.models.forms import RegistrationForm, LoginForm
from flaskblog.models.database import User

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
def home():
    return render_template('pages/index.html', posts=posts, title='Home')


@app.route('/account')
def account():
    return render_template('pages/account.html', title='Account')


@app.route('/about')
def about():
    return render_template('pages/about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Your account has been register. You able to login now.", 'success')
        return redirect(url_for('login'))
    return render_template('auth/register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash(f'Login unsuccessful. Please check your username and password.', 'danger')
    return render_template('auth/login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))