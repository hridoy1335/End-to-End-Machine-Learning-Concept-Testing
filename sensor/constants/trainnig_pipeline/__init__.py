# import dependency
import os


# defining the file name
TARGET_COLUMNS = "class"
PIPELINE_NAME = "sensor"
ARTIFACTS_DIR = "artifacts"
FILE_NAME = "sensor.csv"

# train and test data
TRAIN_FILE_NAME:str = "train.csv"
TEST_FILE_NAME:str = "test.csv"

# defining the preprossesing file name
PREPROCSSING_OBJECT_FILE_NAME = "preprocessing.pkl"
MODEL_FILE_NAME = "model.pkl"
SCHEMA_FILE_PATH = os.path.join("config","schema.yaml")


"""
Data Ingestion related constants file name
""" 
DATA_INGESTION_COLLECTION_NAME: str = "sensor"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FUTURE_STORE_DIR: str = "future_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2