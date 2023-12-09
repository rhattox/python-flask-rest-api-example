from flask import Blueprint

routes = Blueprint('routes', __name__)

@routes.route("/")
def index():
    return "Hello, this is the main page!"

@routes.route("/about")
def about():
    return "This is the about page!"