from flask import render_template, flash, redirect, url_for, request, abort
from flask_login import login_user, login_required, current_user, logout_user
from flask_mail import Message
from flaskblog import app, db, bcrypt, mail
from flaskblog.models.forms import RegistrationForm, LoginForm, ForgotPasswordForm, ResetPasswordForm,\
    UpdateAccountForm, ChangePasswordForm, PostForm
from flaskblog.models.database import User, Post
from PIL import Image
import os
import secrets


@app.route('/')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=4)
    latest_post = Post.query.order_by(Post.date_posted.desc()).first()
    return render_template('pages/index.html', posts=posts, post=latest_post, title='Home')


@app.route('/user/str:<username>')
@login_required
def user_post(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user). \
        order_by(Post.date_posted.desc()).paginate(page=page, per_page=4)
    return render_template('posts/post_by_user.html', title='Home', posts=posts, user=user)


@app.route('/new_post', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    legend = 'New Post'
    if form.validate_on_submit():
        post = Post(title=form.title.data, description=form.desc.data,
                    content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash(f'Your Post "{form.title.data}" has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('posts/new_post.html', title='New Post', form=form, legend=legend)


@app.route('/post/<int:post_id>')
def read_more_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('posts/read_more.html', title=post.title, post=post)


@app.route('/post/<int:post_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash(f'Your Post has been deleted!', 'success')
    return redirect(url_for('home'))


@app.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.description = form.desc.data
        post.content = form.content.data
        db.session.commit()
        flash(f'Your Post has been updated!', 'success')
        return redirect(url_for('read_more_post', post_id=post_id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.desc.data = post.description
        form.content.data = post.content
    return render_template('posts/new_post.html', title='Update Post', form=form, legend='Update Post')


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