from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, db

auth= Blueprint('auth', __name__)


@auth.route('/login', methods= ['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return render_template("base.html")

@auth.route('/sign_up', methods= ['GET', 'POST'])
def sign_up():
    if request.method=='POST':
        email= request.form.get('email')
        username= request.form.get('username')
        password= request.form.get('password')
        confirm_password= request.form.get('confirm_password')

        if len(email)<4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(username)<2:
            flash('Username must be greater than 1 characters.', category='error')
        elif password!=confirm_password:
            flash('Passwords dont match.', category='error')
        elif len(password)<7:
            flash('Password must be greater than 6 characters.', category='error')
        else:
            new_user = User(email=email, username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            #add user to database
            flash('Account Created.', category='success')

            return redirect(url_for('views.home'))

        
    return render_template("sign_up.html")