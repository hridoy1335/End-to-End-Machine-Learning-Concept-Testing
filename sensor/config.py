import os
import pymongo
from dataclasses import dataclass

@dataclass
class read_env:
    mongo_db_uri:str = os.getenv("MONGO_DB_URI")
    mongo_db_name:str = os.getenv("MONGO_DB_NAME")
    mongo_collection_name:str = os.getenv("MONGO_COLLECTION_NAME")
    
env = read_env()

mongo_clint = pymongo.MongoClient(env.mongo_db_uri)
db = mongo_clint[env.mongo_db_name]
collection = db[env.mongo_collection_name]