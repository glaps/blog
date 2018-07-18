from flask import render_template, redirect, flash, url_for
from app import apli
from app.forms import LoginForm


@apli.route("/")
@apli.route("/index")
def index():
    user = "vlad"
    return render_template("index.html",title="BLOG",user=user)


@apli.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for("index"))
    return render_template('login.html', title='Sign In', form=form)
