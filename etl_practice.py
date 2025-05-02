from src import config
from src import logging_utils
from src import extract_utils

############ Transform Methods ############
def transform(data):
    logging_utils.log("In transform(): started")
    
    # Round Price values to 2 decimal places
    data["price"] = round(data["price"], 2)

    logging_utils.log("In transform(): ended")
    return data


############ Load Methods ############
def load_data(target_file, transformed_data):
    logging_utils.log(f"In load_data(): Loading data to file '{target_file}'")
    transformed_data.to_csv(target_file)
    logging_utils.log(f"In load_data(): Done loading data to file '{target_file}'")

############ Main ############

logging_utils.log("ETL Job Started")
extracted_data = extract_utils.extract(config.INPUT_FILES_DIR_PATH)

transformed_data = transform(extracted_data)

load_data(config.OUTPUT_FILE_PATH, transformed_data)

logging_utils.log("ETL Job Ended\n")

