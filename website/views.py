from flask import Blueprint, render_template
from .tasker import greet, Task

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("home.html")


@views.route("/tasks/")
def tasks():
    user = {
            "name": "ToxicFscyther",
            "username": "toxicfs",
    }
    folders = ["CS", "Math"]
    tasks = [
        Task("Specimen", "Start Reactor", "30 seconds from now", "CS"),
        Task("Admin", "Swipe Card", "2 seconds from now", "Math"),
    ]
    return render_template("tasks.html", greeting=greet(), user=user, folders=folders, tasks=tasks)
