from pymongo import MongoClient


class MongoDBController:
    def __init__(self, host, port):
        self.__host = host
        self.__port = port
        self.__database = None
        self.__client = MongoClient(host=host, port=port)

    def set_host(self, host):
        self.__host = host

    def get_host(self):
        return self.__host

    def get_client(self):
        return self.__client

    def get_database(self, database_name):
        self.__database = self.__client[database_name]
        return self.__database

    def get_collection(self, collection_name):
        return self.__database[collection_name]
