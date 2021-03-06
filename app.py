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
    if result is not None and result.inserted_id is not None:
        return json.dumps({'result': True})
    else:
        return json.dumps({'result': False})


@app.route("/users/<string:cpf>")
def get_user(cpf):
    obj_filter = {'cpf': cpf}
    return str(User().get_one(obj_filter=obj_filter))


if __name__ == '__main__':
    app.run()
