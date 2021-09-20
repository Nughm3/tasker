from flask import Blueprint, render_template

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("home.html")


@views.route("/tasks/")
def tasks():
    user = {
        "name": "aaden",
        "username": "Nughm",
    }
    folders = ["CS", "Maths"]
    tasks = [
        {
            "id": 0,
            "folder": 0,
            "title": "Frick Woman",
            "summary": "Get a life",
            "due_date": "69/69/6969",
            "notes": "This time it's about lists!",
        },
    ]

    return render_template(
        "tasks.html",
        user=user,
        folders=[{"id": folders.index(name), "name": name} for name in folders],
        tasks=tasks,
    )
