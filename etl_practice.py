import sys

from src import config
from src import logging_utils
from src import extract_utils
from src import transform_utils
from src import load_utils

logging_utils.log("ETL Job Started")

try:
    extracted_data = extract_utils.extract(config.INPUT_FILES_DIR_PATH)
    extract_utils.validate_extract(extracted_data)

    transformed_data = transform_utils.transform(extracted_data)
    transform_utils.validate_transform(transformed_data)

    load_utils.load(config.OUTPUT_FILE_PATH, transformed_data)
    load_utils.validate_load(config.OUTPUT_FILE_PATH, transformed_data)

except FileNotFoundError as e:
    logging_utils.log(f"Encountered FileNotFoundError: \"{e}\"")
    sys.exit(1)
except ValueError as e:
    logging_utils.log(f"Encountered ValueError: \"{e}\"")
    sys.exit(1)
except AssertionError as e:
    logging_utils.log(f"Encountered AssertionError: \"{e}\"")
    sys.exit(1)

logging_utils.log("ETL Job Ended\n")
