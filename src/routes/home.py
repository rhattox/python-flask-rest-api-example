from flask import Blueprint

home = Blueprint('home', __name__)

@home.route("/")
def index():
    return "Hello, this is the main page!"

@home.route("/about")
def about():
    return "This is the about page!"