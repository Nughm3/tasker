from flask import Blueprint

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return "<h1>Home</h1>"


@views.route("/startpage")
def startpage():
    return "<h1>Startpage</h1>"
