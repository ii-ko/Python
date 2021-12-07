from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, login_required, current_user, logout_user
from flask_mail import Message
from flaskblog import app, db, bcrypt, mail
from flaskblog.models.forms import RegistrationForm, LoginForm, ForgotPasswordForm, ResetPasswordForm
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


@app.route('/new_post')
@login_required
def new_post():
    return render_template('posts/new_post.html', title='New Post')


@app.route('/account')
@login_required
def account():
    return render_template('pages/account.html', title='Account')


@app.route('/about')
def about():
    return render_template('pages/about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash(f'Login unsuccessful. Please check your username and password.', 'danger')
    return render_template('auth/login.html', title='Login', form=form)


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password reset request', sender='csmyauth01@gmail.com', recipients=[user.email])
    msg.body = f''' To reset your password, visit the following link:
    {url_for('reset_password', token=token, _external=True)}
    
    If you did not make this request then simply ignore this email and no change will be made.
    '''
    mail.send(msg)


@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = ForgotPasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash(f"An email has been sent with instruction to reset your password", "info")
        return redirect(url_for('login'))
    return render_template('auth/forgot_password.html', title='Forgot Password', form=form)


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash(f"That is invalid or expired token", "warning")
        return redirect(url_for('forgot_password'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash(f"Your password has been update. You able to login now.", 'success')
        return redirect(url_for('login'))
    return render_template('auth/reset_password.html', title='Reset Password', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))