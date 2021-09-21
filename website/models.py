# from . import db
# from flask_login import UserMixin
# from sqlalchemy.sql import func
#
#
# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(150))
#     password = db.Column(db.String(150))
#     folders = db.relationship("Folder")
#     tasks = db.relationship("Task")
#
#
# class Folder(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(150))
#     user_id = db.Column(db.Integer)
#
#
# class Task(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(150))
#     summary = db.Column(db.String(150))
#     note = db.Column(db.String(5000))
#     due = db.Column(db.DateTime(timezone=True), default=func.now())
#     user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
#     folder_id = db.Column(db.Integer)
