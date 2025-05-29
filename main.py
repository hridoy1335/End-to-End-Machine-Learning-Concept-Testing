import sys
from sensor.logger import logging
from sensor.exception import SensorException
from sensor.utils import push_data_from_mongo_db

# check the logging and exception file is working or not

# def custom_error():
#     try:
#         logging.info('this is demo and test zoro division')
#         1/0
#     except Exception as e:
#         raise SensorException(e,sys)

# pushing the data from mongo db to the csv file

# if __name__ == "__main__":
#     try:
#         logging.info('data push started')
#         file_data_path = "data/sensor_info.csv"
#         push_data_from_mongo_db(file_data_path)
#         logging.info('data push completed')
#     except Exception as e:
#         print(e)