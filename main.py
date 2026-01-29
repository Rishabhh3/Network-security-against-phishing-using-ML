from Network_Security.components.data_ingestion import DataIngestion

from Network_Security.entity.config_entity import DataIngestionConfig , DataValidationConfig , DataTransformationConfig , ModelTrainerConfig
from Network_Security.entity.config_entity import TrainingPipelineConfig
from Network_Security.logger.logger import logger
from Network_Security.exception.exception import NetworkSecurityException

import sys

if __name__=='__main__':
    try:
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        data_ingestion=DataIngestion(data_ingestion_config)
        logger.info("Initiate the data ingestion")
        data_ingestion_artifact = data_ingestion.inititiate_data_ingestion()
        logger.info("Data ingestion completed!!!")


    except Exception as e:
        raise NetworkSecurityException(e,sys)

