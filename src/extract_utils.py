import glob
import os
import pandas as pd 
import xml.etree.ElementTree as ET 

from . import config
from . import logging_utils

def extract_from_csv(file_to_process):
    """Extract car dealership data from CSV file in `file_to_process`

    Keyword Arguments:
    - file_to_process -- path to an CSV file containing fields `car_model`, `year_of_manufacture`, `price`, `fuel`

    Return Values:
    - pandas DataFrame containing extracted data
    """

    logging_utils.log(f"In extract_from_csv(): Extracting from file '{file_to_process}'")
    try:
        dataframe = pd.read_csv(file_to_process, usecols=config.COLUMN_NAMES)
    except ValueError as e:
        raise ValueError(f"Expected columns '{config.COLUMN_NAMES}' not found in file '{file_to_process}'")
    return dataframe

def extract_from_json(file_to_process):
    """Extract car dealership data from JSON file in `file_to_process`

    Keyword Arguments:
    - file_to_process -- path to an JSON file containing fields `car_model`, `year_of_manufacture`, `price`, `fuel`

    Return Values:
    - pandas DataFrame containing extracted data
    """

    logging_utils.log(f"In extract_from_json(): Extracting from file '{file_to_process}'")
    dataframe = pd.read_json(file_to_process, lines=True)

    return dataframe

def extract_from_xml(file_to_process):
    """Extract car dealership data from XML file in `file_to_process`

    Keyword Arguments:
    - file_to_process -- path to an XML file containing fields `car_model`, `year_of_manufacture`, `price`, `fuel`

    Return Values:
    - pandas DataFrame containing extracted data
    """
    logging_utils.log(f"In extract_from_xml(): Extracting from file '{file_to_process}'")
    rows_list = []
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    for car in root:
        car_model = str(car.find("car_model").text)
        year_of_manufacture = int(car.find("year_of_manufacture").text)
        price = float(car.find("price").text)
        fuel = str(car.find("fuel").text)

        rows_list.append({"car_model":car_model, "year_of_manufacture":year_of_manufacture, "price":price, "fuel":fuel})

    return pd.DataFrame.from_dict(rows_list)

def extract(input_files_dir_path):
    """Extract data from CSV, JSON, and XML files in `input_files_dir_path` specified into a single dataframe

    Keyword Arguments:
    - input_files_dir_path -- relative path with respect to repository root to directory containing input files
        - supported file formats: CSV, JSON, XML
    
    Return Values:
    - a Pandas DataFrame containing all extracted data
    """
    logging_utils.log("In extract(): started")

    if os.path.exists(input_files_dir_path) != True:
        logging_utils.log(f"In extract(): ERROR: Input file path '{input_files_dir_path}' does not exist")
        raise FileNotFoundError(f"Input file path '{input_files_dir_path}' does not exist")

    # Create empty data frame with the corresponding headers
    extracted_dfs_list = []

    # Process all CSV files
    logging_utils.log("In extract(): start processing CSV files")
    num_files_processed = 0
    for csvfile in glob.glob(f"{input_files_dir_path}\\*.csv"):
        extracted_dfs_list.append(extract_from_csv(csvfile))
        num_files_processed += 1
    logging_utils.log(f"In extract(): done processing {num_files_processed} CSV files")

    # Process all JSON files
    num_files_processed = 0
    logging_utils.log("In extract(): start processing JSON files")
    for jsonfile in glob.glob(f"{input_files_dir_path}\\*.json"):
        extracted_dfs_list.append(extract_from_json(jsonfile))
        num_files_processed += 1
    logging_utils.log(f"In extract(): done processing {num_files_processed} JSON files")

    # Process all XML files
    num_files_processed = 0
    logging_utils.log("In extract(): start processing XML files")
    for xmlfile in glob.glob(f"{input_files_dir_path}\\*.xml"):
        extracted_dfs_list.append(extract_from_xml(xmlfile))
        num_files_processed += 1
    logging_utils.log(f"In extract(): done processing {num_files_processed} XML files")

    try: 
        # Concatenate all dataframes in the extracted_dfs_list
        # into a single DataFrame
        # Note that ignore_index is set to True so that the index is rebuilt with properly incrementing values
        extracted_data = pd.concat(extracted_dfs_list, ignore_index=True)
    except ValueError as e:
        logging_utils.log(f"In extract(): ERROR: No input files found in path '{input_files_dir_path}'")
        raise FileNotFoundError(f"No input files found in path '{input_files_dir_path}'")

    logging_utils.log("In extract(): ended")
    return extracted_data

def validate_extract(test_df):
    logging_utils.log("In validate_extract(): started")

    # Assert expected number of columns
    assert (test_df.shape[1] == len(config.COLUMN_NAMES)), f"validate_extract(): Required number of columns is '{len(config.COLUMN_NAMES)}' but found '{test_df.shape[1]}'"

    # Assert expected columns exist in result
    for column in config.COLUMN_NAMES:
        assert (column in test_df.columns), f"validate_extract(): Required column '{column}' not found in extracted dataframe"

    logging_utils.log("In validate_extract(): ended")
