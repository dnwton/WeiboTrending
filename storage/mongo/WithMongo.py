from pymongo import MongoClient


class WithMongo:

    def get_mongo(self, mongo_host, mongo_port):
        mongo_client = MongoClient(host=mongo_host, port=mongo_port)
        return mongo_client

    def save_mongo(self, database, collection, metadata):
        collection = database[collection]
        collection.insert_one(metadata)
