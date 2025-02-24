from dashboardPackage import app
from flask import render_template, redirect, url_for, flash
from dashboardPackage.models import Customers, Item, User, Taps
from dashboardPackage.forms import RegisterForm, LoginForm
from dashboardPackage import db
from flask_login import login_user, logout_user, login_required

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')


@app.route("/dashboard")
@login_required
def dashboard_page():
    taps = Taps.query.all()
    return render_template('dashboard.html', taps=taps)

@app.route("/customers")
@login_required
def customers_page():
    customers = Customers.query.all()
    return render_template('customers.html', customers=customers)


@app.route('/register', methods=['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password = form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()

        login_user(user_to_create)
        flash(f'Account created successfully! You are logged in as{user_to_create.username}', category='success')

        return redirect(url_for('dashboard_page'))
    if form.errors !={}:
        for err_msg in form.errors.values():
            flash(f'There was an error while creating user: {err_msg}', category='danger')
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET','POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('dashboard_page'))
        else:
            flash('Username and password are not match! Please try again', category='danger')

    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out", category='info')
    return redirect(url_for('home_page'))

