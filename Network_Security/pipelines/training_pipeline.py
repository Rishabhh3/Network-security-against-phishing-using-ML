import os
import sys
from Network_Security.logger.logger import logger
from Network_Security.exception.exception import NetworkSecurityException
from Network_Security.components.data_ingestion import DataIngestion
from Network_Security.components.data_transformation import DataTransformation
from Network_Security.components.data_validation import DataValidation
from Network_Security.components.model_trainer import ModelTrainer
from Network_Security.entity.config_entity import TrainingPipelineConfig , DataIngestionConfig , DataTransformationConfig , DataValidationConfig , ModelTrainerConfig
from Network_Security.entity.artifact_entity import *

class TrainingPipeline:
    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            self.data_ingestion_config = DataIngestionConfig(self.training_pipeline_config)
            logger.info("Start Data Ingestion")
            data_ingestion = DataIngestion(self.data_ingestion_config)
            self.data_ingestion_artifact = data_ingestion.inititiate_data_ingestion()
            logger.info("Data ingestion completed !!!")
            
            return self.data_ingestion_artifact

        except Exception as e:
            raise NetworkSecurityException(e,sys)
    

    def start_data_validation(self) -> DataValidationArtifact:
        try:
            
            self.data_validation_config = DataValidationConfig(self.training_pipeline_config)
            data_validation = DataValidation(self.data_ingestion_artifact , self.data_validation_config)
            self.data_validation_artifact = data_validation.initiate_data_validation()

            return self.data_validation_artifact
            
            

        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def start_data_transformation(self) -> DataTransformationArtifact:
        try:

            self.data_transformation_config = DataTransformationConfig(self.training_pipeline_config)
            data_transformation = DataTransformation(self.data_validation_artifact
                                                      ,self.data_transformation_config)
            self.data_transformation_artifact = data_transformation.initiate_data_transformation()

            return self.data_transformation_artifact

            

        except Exception as e:
            raise NetworkSecurityException(e,sys)
    

    def start_model_training(self) -> ModelTrainerArtifact:
        try:

            self.model_training_config = ModelTrainerConfig(self.training_pipeline_config)
            model_trainer = ModelTrainer(self.model_training_config ,self.data_transformation_artifact )
            self.model_trainer_artifact = model_trainer.initiate_model_trainer()

            return self.model_trainer_artifact

            
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation()
            data_transformation_artifact = self.start_data_transformation()
            model_trainer_artifact=self.start_model_training()
    
            return model_trainer_artifact
    
        except Exception as e:
            raise NetworkSecurityException(e,sys)


if __name__ == "__main__":
    obj = TrainingPipeline()
    model_trainer_artifact = obj.run_pipeline()
        
