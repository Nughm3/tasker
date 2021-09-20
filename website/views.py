from flask import Blueprint, render_template
from datetime import datetime

views = Blueprint("views", __name__)

def due_date():
    current_date = datetime.strftime(datetime.now(), "%d-%m-%Y")
    duedate = 0

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
            "due_date": "11/09/23",
            "notes": "This time it's about lists!",
        },
    ]

    return render_template(
        "tasks.html",
        user=user,
        folders=[{"id": folders.index(name), "name": name} for name in folders],
        tasks=tasks,
        maintask = {
            "id": 123,
            "category": 0,
            "priority": 1,
            "status": 0,
            "title": "test",
            "due": "23-23-2323",
            "reminder": 2,
            "created": "34-34-34",
        }
    )
