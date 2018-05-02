from utils.MongoDBController import MongoDBController


class BaseModel:
    def __init__(self):
        self.__mongo_client = MongoDBController()

    def get_mongo_client(self):
        return self.__mongo_client

    def set_mongo_client(self, mongo_client):
        self.__mongo_client = mongo_client

    def save(self):
        pass

    def get_all(self):
        pass

    def get_one(self, obj_filter):
        pass
