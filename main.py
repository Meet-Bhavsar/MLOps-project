from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation, DataValidationConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig
import os
import sys

if __name__ == '__main__':
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiating data ingestion")
        
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()  # <-- missing this step before
        
        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(data_ingestion_artifact, data_validation_config)  # <-- corrected
        data_validation_artifact = data_validation.initiate_data_validation()
        
        logging.info("Data validation completed")
        print(data_validation_artifact)

    except Exception as e:
        raise NetworkSecurityException(e, sys)
