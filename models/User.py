from models.BaseModel import BaseModel


class User(BaseModel):
    def __init__(self):
        super().__init__()
        self.__name = None
        self.__cpf = None
        self.__address = None
        self.__cep = None
        self.__phone = None
        self.__cellular = None

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_cep(self):
        return self.__cep

    def set_cep(self, cep):
        self.__cep = cep

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone

    def set_cellular(self, cellular):
        self.__cellular = cellular

    def get_cellular(self):
        return self.__cellular

    def get_all(self):
        client = self.get_mongo_client()
        db = client.get_database("test")
        collection = db["users"]
        return collection.find()

    def get_one(self, obj_filter):
        client = self.get_mongo_client()
        db = client.get_database("test")
        collection = db["users"]
        return collection.find_one(obj_filter)

    def save(self):
        client = self.get_mongo_client()
        db = client.get_database("test")
        collection = db["users"]
        new_user = {"name": self.__name,
                    "cpf": self.__cpf,
                    "address": self.__address,
                    "cep": self.__cep,
                    "phone": self.__phone,
                    "cellular": self.__cellular}
        return collection.insert_one(new_user)
