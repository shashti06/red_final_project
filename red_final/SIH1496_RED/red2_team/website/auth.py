from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Message
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.pt100'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/upevents')
@login_required
def upevents():
    return redirect(url_for('views.upevents'))


@auth.route('/about')
@login_required
def about():
    return redirect(url_for('views.about'))

@auth.route('/register')
@login_required
def register():
    return redirect(url_for('views.register'))

@auth.route('/curated0')
@login_required
def curated():
    return redirect(url_for('views.curated0'))

@auth.route('/curated1')
@login_required
def curated1():
    return redirect(url_for('views.curated1'))

@auth.route('/curated2')
@login_required
def curated2():
    return redirect(url_for('views.curated2'))

@auth.route('/curated3')
@login_required
def curated3():
    return redirect(url_for('views.curated3'))


@auth.route('/periodt')
@login_required
def period():
    return redirect(url_for('views.periodt'))



@auth.route('/epfor')
@login_required
def epfor():
    return redirect(url_for('views.epfor'))


@auth.route('/map1')
@login_required
def map1():
    return redirect(url_for('views.map1'))

@auth.route('/game')
@login_required
def game():
    return redirect(url_for('views.game'))

@auth.route('/rthank')
@login_required
def rthank():
    return redirect(url_for('views.rthank'))

@auth.route('/redeem1')
@login_required
def redeem1():
    return redirect(url_for('views.redeem1'))

@auth.route('/discount-page')
@login_required
def discount_page():
    return redirect(url_for('views.discount-page'))



@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(username) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(
                password1, method='scrypt'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.pt100'))

    return render_template("sign_up.html", user=current_user)

