from . import logging_utils

def load(target_file, transformed_data):
    logging_utils.log(f"In load_data(): Loading data to file '{target_file}'")
    transformed_data.to_csv(target_file)
    logging_utils.log(f"In load_data(): Done loading data to file '{target_file}'")
