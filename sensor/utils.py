# importing dependency
import pandas as pd
from sensor.logger import logging
from sensor.config import collection
from sensor.exception import SensorException


def push_data_from_mongo_db(file_path:str)->None:
    try:
        df = pd.read_csv(file_path)
        logging.info(f"File loaded successfully")
        data = df.to_dict(orient='records')
        logging.info(f"Data converted to json format")
        collection.insert_many(data)
        logging.info(f"Data pushed to MongoDB successfully")
    except Exception as e:
        raise SensorException(e,stacks=[logging]) from e