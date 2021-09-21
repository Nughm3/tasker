from flask import Blueprint, render_template, request
from . import db_read, db_write

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("home.html")

@views.route("/tasks/")
def tasks():
    if "folderid" in request.values:
        folderid = request.values["folderid"]
    else:
        folderid = 0

    user = {
        "name": "Aaden",
        "username": "Nughm",
    }
    print(db_read("SELECT * FROM accounts;"))
    # users can't be implemented here yet until login system is done

    folders = db_read("SELECT * FROM folders ORDER BY name;")
    tasks = db_read(f"SELECT * FROM tasks WHERE folderid='{folderid}' ORDER BY title;")

    folders = [{"id": folders.index(name), "name": name["name"]} for name in folders]

    return render_template(
        "tasks.html",
        user = user,
        folders = folders,
        tasks = tasks,
        maintask = {
            "id": 123,
            "category": 0,
            "priority": 1,
            "status": 0,
            "title": "test",
            "due": "23/23/2323",
            "reminder": 2,
            "created": "34/34/3434",
        },
    )
