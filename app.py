from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "To be implemented"


def get_users():
    pass