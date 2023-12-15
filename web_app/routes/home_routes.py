# this is the "web_app/routes/home_routes.py" file...

from flask import Blueprint, request, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
    #return "Welcome Home"
    return render_template("home.html")

@home_routes.route("/profsearch")
def about():
    print("Search...")
    return render_template("search.html")

@home_routes.route("/classsearch")
def about2():
    print("Search...")
    return render_template("class_search.html")