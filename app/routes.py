
from flask import render_template
from app import apli

@apli.route("/")
@apli.route("/index")
def index():
    user = "vlad"
    return render_template("index.html",title="BLOG",user=user)