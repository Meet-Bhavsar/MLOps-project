import os
import sys
import pandas as pd
import numpy as np

# defining column constants for training pipelin
TARGET_COLUMN = 'Result'
PIPELINE_NAME: str = 'NetworkSecurity'
ARTIFACT_DIR: str = 'Artifacts'
FILE_NAME: str = 'phisingData.csv'

TRAIN_FILE_NAME: str = 'train.csv'
TEST_FILE_NAME: str = 'test.csv'
PREPROCESSING_OBJECT_FILE_NAME: str = "preprocessor.pkl"
SCHEMA_FILE_PATH = os.path.join("data_schema", "schema.yaml")

# data ingestion related constants 
DATA_INGESTION_COLLECTION_NAME:str = 'NetworkData'
DATA_INGESTION_DATABASE_NAME:str = 'meet'
DATA_INGESTION_DIR_NAME:str = 'data_ingestion'
DATA_INGESTION_FEATURE_STORE_DIR:str = 'feature_store'
DATA_INGESTION_FEATURE_FILE_NAME:str = 'phisingData.csv'
DATA_INGESTION_INJESTED_DIR:str = 'ingested'
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float = 0.2 

# data validation related constants
DATA_VALIDATION_DIR_NAME:str = 'data_validation'
DATA_VALIDATION_VALID_DIR:str = 'validated'
DATA_VALIDATION_INVALID_DIR:str = 'invalid'
DATA_VALIDATION_DRIFT_REPORT_DIR:str = 'drift_report'
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME:str = 'report.yaml'

# data transformation related constants
DATA_TRANSFORMATION_DIR_NAME:str = 'data_transformation'
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR:str = 'transformed'
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR:str = 'transformed_object'
DATA_TRAMSFORMATION_IMPUTER_PARAMS:dict ={
    "missing_values": np.nan,
    "n_neighbors": 3,
    "weights": "uniform",
}
