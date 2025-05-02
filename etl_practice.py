from src import config
from src import logging_utils
from src import extract_utils
from src import transform_utils
from src import load_utils

logging_utils.log("ETL Job Started")
extracted_data = extract_utils.extract(config.INPUT_FILES_DIR_PATH)

transformed_data = transform_utils.transform(extracted_data)

load_utils.load(config.OUTPUT_FILE_PATH, transformed_data)

logging_utils.log("ETL Job Ended\n")
