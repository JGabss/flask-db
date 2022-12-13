from app import app
from flask import request, render_template, redirect, url_for
from models import User

@app.route("/")
def index():
    data = User.query.order_by(User.id).all()
    return render_template("index.html", users=data)

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        User.create(username, password)

        return redirect(url_for("index"))

    return render_template("form.html")