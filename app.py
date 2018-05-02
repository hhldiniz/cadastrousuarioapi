from flask import Flask

from models.User import User

app = Flask(__name__)


@app.route("/")
def index():
    return "To be implemented"


@app.route("/users")
def get_users():
    return User().get_all()


@app.route("/users/new")
def new_users():
    pass


@app.route("/users/<string:id>")
def get_user(obj_id):
    return User().get_one({"_id": obj_id})
