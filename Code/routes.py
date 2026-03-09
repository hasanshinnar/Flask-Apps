from flask import render_template, abort, redirect, url_for
from Code import app


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/user/<username>")
def user(username):
    return render_template("user.html", username=username)


@app.route("/user/<int:userid>")
def user_id(userid):
    if userid > 1000:
        abort(404)
    else:
        return render_template("user.html", userid=userid)


@app.route("/go-home")
def go_home():
    return redirect(url_for("home"))


@app.route("/products")
def products():
    products = [
        {"name": "Product 1", "price": 19.99, "in_stock": True},
        {"name": "Product 2", "price": 29.99, "in_stock": False},
        {"name": "Product 3", "price": 39.99, "in_stock": True},
    ]
    return render_template("products.html", products=products)
