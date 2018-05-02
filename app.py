import json

from flask import Flask, request

from models.User import User

app = Flask(__name__)


@app.route("/")
def index():
    return "To be implemented"


@app.route("/users")
def get_users():
    return str(User().get_all())


@app.route("/users/new", methods=["POST"])
def new_user():
    request_params = json.loads(json.dumps(request.form))
    name = request_params["name"]
    cpf = request_params["cpf"]
    address = request_params["address"]
    cep = request_params["cep"]
    phone = request_params["phone"]
    cellular = request_params["cellular"]
    user = User()
    user.set_name(name)
    user.set_cpf(cpf)
    user.set_address(address)
    user.set_cep(cep)
    user.set_phone(phone)
    user.set_cellular(cellular)
    result = user.save()
    if result.inserted_id is not None:
        return json.dumps({'result': True})
    else:
        return json.dumps({'result': False})


@app.route("/users/<string:obj_id>")
def get_user(obj_id):
    return User().get_one({"_id": obj_id})


if __name__ == '__main__':
    app.run()
