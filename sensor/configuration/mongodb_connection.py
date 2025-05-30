import os
import certifi
import logging
from dotenv import load_dotenv
from pymongo import MongoClient
from sensor.constants.database import *
from sensor.constants.env_variable import *

load_dotenv()
ca = certifi.where()


class MongoDBClient:
    client = None
    
    def __init__(self,data_base_name = MONGODB_DB_NAME_KEY) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_uri = os.getenv(MONGODB_URI_KEY)
                logging.info(f"Retrieved MongoDB URL: {mongo_db_uri}")
                if "localhost" in mongo_db_uri:
                    MongoDBClient.client = MongoClient(mongo_db_uri)
                else:
                    MongoDBClient.client = MongoClient(mongo_db_uri,tlsCAFile = ca)
                    
            self.client = MongoDBClient.client
            self.database = self.client[MONGODB_DB_NAME_KEY]
            self.collection = self.database[MONGODB_COLLECTION_NAME_KEY]
                    
        except Exception as e:
            logging.error(f"Error initializing MongoDB client: {e}")
            raise