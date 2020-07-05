from flask import render_template, url_for, request, session, redirect, flash, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from ..models.models import User, Match
from ..forms.login_form import LoginForm
from ..forms.register_form import RegisterForm

users = Blueprint('users', __name__)


@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            form.check_email(form.email)
            form.check_username(form.username)
            pass_hash = generate_password_hash(form.password.data)
            user = User(username=form.username.data, email=form.email.data, pass_hash=pass_hash)
            db.session.add(user)
            db.session.commit()
            flash("Registration successful, you can login now")
            # flash("Admin is notified!")
            return redirect(url_for('users.login'))
        except Exception as e:
            flash(e, "danger")
    # for fieldName, errorMessages in form.errors.items():
    #    flash(errorMessages, "danger")
    return render_template('register.html', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None:
            if check_password_hash(user.pass_hash, form.password.data) is True:
                login_user(user)
                # session.logged_in = True # Alternative approach to save user login - session based

                # next_url is something user is trying to access before login, (where @login_required is added for the view),
                # then the page will be directed to login and after login we are fetching the url the was accessed and redirecting to it.
                next_url = request.args.get('next')
                if(next_url == None or next_url[0] == '/'):
                    next_url = url_for('core.home')
                return redirect(next_url)
            else:
                flash("Invalid password")
        else:
            flash("Invalid email")
    for fieldName, errorMessages in form.errors.items():
        flash(errorMessages, "danger")
    return render_template('login.html', form=form)


@users.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    # session.logged_in = False # Alternative approach to save user login - session based
    return render_template('home.html')
