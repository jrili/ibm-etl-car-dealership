import glob 
import pandas as pd 
import xml.etree.ElementTree as ET 
from datetime import datetime 

LOG_FILE = "log_file.txt"
TARGET_FILE = "transformed_data.csv"

############ Logging Methods ############
def log(msg, console_enabled=True):
    timestamp_format = "%Y-%h-%d-%H:%M:%S"
    now = datetime.now()
    timestamp_str = now.strftime(timestamp_format)

    with open(LOG_FILE, "a") as f:
        log_str = timestamp_str + "," + msg
        if console_enabled:
            print(log_str)
        f.write(log_str + "\n")


############ Extract Methods ############

def extract_from_csv(file_to_process):
    log(f"In extract_from_csv(): Extracting from file '{file_to_process}'")
    dataframe = pd.read_csv(file_to_process)
    return dataframe

def extract_from_json(file_to_process):
    log(f"In extract_from_json(): Extracting from file '{file_to_process}'")
    dataframe = pd.read_json(file_to_process, lines=True)
    return dataframe

def extract_from_xml(file_to_process):
    log(f"In extract_from_xml(): Extracting from file '{file_to_process}'")
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

def extract():
    log("In extract(): started")
    # Create empty data frame with the corresponding headers
    extracted_dfs_list = []

    # Process all CSV files
    log("In extract(): start processing CSV files")
    for csvfile in glob.glob("datasource\*.csv"):
        extracted_dfs_list.append(extract_from_csv(csvfile))
    log("In extract(): done processing CSV files")

    # Process all JSON files
    log("In extract(): start processing JSON files")
    for jsonfile in glob.glob("datasource\*.json"):
        extracted_dfs_list.append(extract_from_json(jsonfile))
    log("In extract(): done processing JSON files")

    # Process all XML files
    log("In extract(): start processing XML files")
    for xmlfile in glob.glob("datasource\*.xml"):
        extracted_dfs_list.append(extract_from_xml(xmlfile))
    log("In extract(): done processing XML files")

    # Concatenate all dataframes in the extracted_dfs_list
    # into a single DataFrame
    # Note that ignore_index is set to True so that the index is rebuilt with properly incrementing values
    extracted_data = pd.concat(extracted_dfs_list, ignore_index=True)

    log("In extract(): ended")
    return extracted_data

############ Transform Methods ############
def transform(data):
    log("In transform(): started")
    
    # Round Price values to 2 decimal places
    data["price"] = round(data["price"], 2)

    log("In transform(): ended")
    return data


############ Load Methods ############
def load_data(target_file, transformed_data):
    log(f"In load_data(): Loading data to file '{target_file}'")
    transformed_data.to_csv(target_file)
    log(f"In load_data(): Done loading data to file '{target_file}'")



############ Main ############

log("ETL Job Started")
extracted_data = extract()

transformed_data = transform(extracted_data)

load_data(TARGET_FILE, transformed_data)

log("ETL Job Ended\n")

