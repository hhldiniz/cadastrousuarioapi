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
        # TODO usar filtro para remover id da resposta
        cursor = collection.find()
        result = []
        for obj in cursor:
            result.append(obj)
        return result

    def get_one(self, obj_filter):
        client = self.get_mongo_client()
        db = client.get_database("test")
        collection = db["users"]
        return collection.find_one(obj_filter)

    def save(self):
        client = self.get_mongo_client()
        db = client.get_database("test")
        collection = db["users"]
        if self.validate_cpf(self.__cpf):
            new_user = {"name": self.__name,
                        "cpf": self.__cpf,
                        "address": self.__address,
                        "cep": self.__cep,
                        "phone": self.__phone,
                        "cellular": self.__cellular}
            return collection.insert_one(new_user)
        else:
            return None

    @staticmethod
    def validate_cpf(cpf):
        cpf_list = list(cpf)
        sum_sequence = 10
        sum_result = 0
        first_flag = False
        second_flag = False
        count = 0
        while count < 9:
            char_as_int = int(cpf_list.__getitem__(count))
            char_as_int = char_as_int * sum_sequence
            sum_result += char_as_int
            sum_sequence -= 1
            count += 1
        first_digit_validation = (sum_result * 10) % 11
        if int(cpf_list.__getitem__(cpf_list.__len__() - 2)) == first_digit_validation:
            first_flag = True
        sum_result = 0
        sum_sequence = 11
        count = 0
        while count < 10:
            char_as_int = int(cpf_list.__getitem__(count))
            char_as_int = char_as_int * sum_sequence
            sum_result += char_as_int
            sum_sequence -= 1
            count += 1
        second_digit_validation = (sum_result * 10) % 11
        if int(cpf_list.__getitem__(cpf_list.__len__() - 1)) == second_digit_validation:
            second_flag = True
        return first_flag and second_flag
