from pymongo import MongoClient

class DB:
    __instance__ = None

    @staticmethod
    def get_instance():
        if DB.__instance__ is None:
            DB()
        return DB.__instance__

    def __init__(self):
        DB.__instance__ = self
        self.client = MongoClient(host=self.connection_url())

    def get_database(self):
        return self.client["GroupChat"]

    def connection_url(self):
        return "mongodb+srv://admin:admin123@cluster0.6uq1zvp.mongodb.net/GroupChat?retryWrites=true&w=majority"
