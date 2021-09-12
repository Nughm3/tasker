from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "tasker.db"


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "asdf"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .models import User, Folder, Task

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/account")

    return app


def create_database(app):
    if not path.exists(f"website/{DB_NAME}"):
        db.create_all(app=app)
        print("Database created")
