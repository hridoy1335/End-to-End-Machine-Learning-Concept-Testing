import os
from datetime import datetime
from sensor.constants.trainnig_pipeline import *


class TrainingPipelineConfig:
    def __init__(self,timestamp = datetime):
        timestamp = timestamp.now().strftime("%d-%m-%Y-%H:%M:%S")
        self.pipeline_name = PIPELINE_NAME
        self.artifacts_dir = os.path.join(ARTIFACTS_DIR,timestamp)
        self.timestamp:str = timestamp
    
class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        # make the data ingestion dir to save the data
        self.data_ingestion_dir: str = os.path.join(training_pipeline_config.artifacts_dir,DATA_INGESTION_DIR_NAME)
        # make the future store data in the data ingestion dir
        self.feature_store_file_path: str = os.path.join(self.data_ingestion_dir,DATA_INGESTION_FUTURE_STORE_DIR,FILE_NAME)
        # make the train.csv file in data ingestion ingested dir
        self.training_file_path: str = os.path.join(self.data_ingestion_dir,DATA_INGESTION_INGESTED_DIR,TRAIN_FILE_NAME)
        # make the test.csv file in data ingestion ingested dir
        self.testing_file_path: str = os.path.join(self.data_ingestion_dir,DATA_INGESTION_INGESTED_DIR,TEST_FILE_NAME)
        # make the train_test_split ratio
        self.train_test_split_ratio: float = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        # make the collection file name
        self.collection_name: str = DATA_INGESTION_COLLECTION_NAME
        