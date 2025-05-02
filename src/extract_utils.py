import glob 
import pandas as pd 
import xml.etree.ElementTree as ET 

from . import logging_utils

def extract_from_csv(file_to_process):
    logging_utils.log(f"In extract_from_csv(): Extracting from file '{file_to_process}'")
    dataframe = pd.read_csv(file_to_process)
    return dataframe

def extract_from_json(file_to_process):
    logging_utils.log(f"In extract_from_json(): Extracting from file '{file_to_process}'")
    dataframe = pd.read_json(file_to_process, lines=True)
    return dataframe

def extract_from_xml(file_to_process):
    logging_utils.log(f"In extract_from_xml(): Extracting from file '{file_to_process}'")
    rows_list = []
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    for car in root:
        car_model = str(car.find("car_model").text)
        year_of_manufacture = int(car.find("year_of_manufacture").text)
        price = float(car.find("price").text)
        fuel = car.find("fuel").text

        rows_list.append({"car_model":car_model, "year_of_manufacture":year_of_manufacture, "price":price, "fuel":fuel})

    return pd.DataFrame.from_dict(rows_list)

def extract(input_files_dir_path):
    logging_utils.log("In extract(): started")
    # Create empty data frame with the corresponding headers
    extracted_dfs_list = []

    # Process all CSV files
    logging_utils.log("In extract(): start processing CSV files")
    for csvfile in glob.glob(f"{input_files_dir_path}\\*.csv"):
        extracted_dfs_list.append(extract_from_csv(csvfile))
    logging_utils.log("In extract(): done processing CSV files")

    # Process all JSON files
    logging_utils.log("In extract(): start processing JSON files")
    for jsonfile in glob.glob(f"{input_files_dir_path}\\*.json"):
        extracted_dfs_list.append(extract_from_json(jsonfile))
    logging_utils.log("In extract(): done processing JSON files")

    # Process all XML files
    logging_utils.log("In extract(): start processing XML files")
    for xmlfile in glob.glob(f"{input_files_dir_path}\\*.xml"):
        extracted_dfs_list.append(extract_from_xml(xmlfile))
    logging_utils.log("In extract(): done processing XML files")

    # Concatenate all dataframes in the extracted_dfs_list
    # into a single DataFrame
    # Note that ignore_index is set to True so that the index is rebuilt with properly incrementing values
    extracted_data = pd.concat(extracted_dfs_list, ignore_index=True)

    logging_utils.log("In extract(): ended")
    return extracted_data
