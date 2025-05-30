import sys
from sensor.logger import logging
from sensor.exception import SensorException
from sensor.components.data_ingestion import DataIngestion
from sensor.entity.artifacts_entity import DataIngestionArtifacts
from sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig


class TrainPipeline:

    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()


    def start_data_ingestion(self)->DataIngestionArtifacts:
        try:
            
            self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)

            logging.info("Starting data ingestion")

            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)

            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

            logging.info(f"Data ingestion completed and artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact
        except  Exception as e:
            raise  SensorException(e,sys)
        
        
    def run_pipeline(self):
        try:
             data_ingestion_artifact:DataIngestionArtifacts = self.start_data_ingestion()
        except Exception as e :    
            raise  SensorException(e,sys)