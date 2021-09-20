from flask import Blueprint, render_template
from datetime import datetime

views = Blueprint("views", __name__)

current_date = datetime.strptime(datetime.now(), "%d-%m-%Y")

@views.route("/")
def home():
    return render_template("home.html")


@views.route("/tasks/")
def tasks():
    user = {
        "name": "Fscyther",
        "username":"Isaac Hung",
    }
    folders = ["CS", "Maths"]
    tasks = [
        {
            "id": 0,
            "folder": 0,
            "title": "CS To Do List",
            "summary": "Do homework",
            "current_date": current_date,
            "due_date": "Your Mom",
            "notes": "This time it's about lists!",
        },
    ]

    return render_template(
        "tasks.html",
        user=user,
        folders=[{"id": folders.index(name), "name": name} for name in folders],
        tasks=tasks,
    )
