from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, login_required, current_user, logout_user
from flask_mail import Message
from flaskblog import app, db, bcrypt, mail
from flaskblog.models.forms import RegistrationForm, LoginForm, ForgotPasswordForm, ResetPasswordForm,\
    UpdateAccountForm, ChangePasswordForm, PostForm
from flaskblog.models.database import User
from PIL import Image
import os
import secrets



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
    form = PostForm()
    legend = 'New Post'
    return render_template('posts/new_post.html', title='New Post', form=form, legend=legend)


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/dist/img', picture_fn)
    output_size = (125, 125)
    img = Image.open(form_picture)
    img.thumbnail(output_size)
    rgb_im = img.convert('RGB')
    rgb_im.save(picture_path)
    return picture_fn


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash(f'Your Account has been updated!.', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='/dist/img/'+current_user.image_file)
    return render_template('pages/account.html', title='Account', image_file=image_file, form=form)


@app.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=current_user.email).first()
        if bcrypt.check_password_hash(user.password, form.old_password.data):
            hashed_password = bcrypt.generate_password_hash(form.new_password.data).decode('utf-8')
            user.password = hashed_password
            db.session.commit()
            flash(f"The password has been update!", 'success')
            return redirect(url_for('account'))
        else:
            flash(f"The new password and old password are not match. Please try again", 'danger')
            return redirect(url_for('change_password'))
    return render_template('pages/change_password.html', title='Change Password', form=form)


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