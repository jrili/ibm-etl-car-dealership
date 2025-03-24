# ETL Project: Car Dealership Data
_Instructions and dataset taken from IBM's [Python Project for Data Engineering](https://www.coursera.org/learn/python-project-for-data-engineering) from Coursera_

# Links
|     Item       |   Link   |
| -------------- | ---------|
|Course Link | [IBM: Python Project for Data Engineering (Coursera)](https://www.coursera.org/learn/python-project-for-data-engineering) |
| Dataset (multiple formats) | https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/datasource.zip |
| Author's Course Completion Certificate|[Certificate](https://www.coursera.org/account/accomplishments/verify/TFH7N05KO7D3) |
| Author's Data Engineer Portfolio | [jrili/data-engineer-portfolio](https://github.com/jrili/data-engineer-portfolio) |

# Dataset Details
| Column Name | Data Type | Details                        | Expected Output |
| ----------- | --------- |------------------------------- | --------------- |
| car_model | string | Name of the car model  | as-is input |
| year_of_manufacture | integer | year when car was manufactured | as-is input |
| price | float | price of car of an unspecified currency | price rounded to 2 decimal places |
| fuel | enum (Petroleum, Disel) | fuel type compatible with car | as-is input |

# Prerequisite Steps
## 1.  Gather the data files
```
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/datasource.zip
```
_Also available with sample outputs and explanations in notebook: [etl_heights_weights.ipynb](https://github.com/jrili/ibm-etl-heights-weights/blob/master/etl_heights_weights.ipynb)_

> [!NOTE]
> In case of unavailability, a snapshot of datasource.zip is also available in the root directory.
> Date of snapshot: `2025 Mar 24`

## 2. Unzip the downloaded file into a directory named `datasource`
```
unzip source.zip -d datasource
```

## 3. Install required libraries
```
python -m pip install -r requirements.txt
```

# Project Tasks

## 1. Extraction
Develop functions to extract from different file formats:
- `extract_from_csv()`
- `extract_from_json()`
- `extract_from_xml()`

## 2. Transformation
Ensure all values taken from different sources are uniform:
- Price must be rounded to 2 decimal places

## 3. Loading
Store the extracted and transformed data into a single CSV file

## 4. Logging
Create a `log_progress()` function that writes the following to a log file:
- event details
- current date and time at time of event

# How to execute:
_(Tested in Python 3.13)_
```
python etl_practice.py
```
_Also available with sample outputs and explanations in notebook: [etl_car_dealership.ipynb](https://github.com/jrili/ibm-etl-car-dealership/blob/master/etl_car_dealership.ipynb)_

# Acknowledgements
## Course Instructors
- Ramesh Sannareddy
- Joseph Santarcangelo
- Abhishek Gagneja
## Course Offered By
* [IBM Skills Network](https://www.coursera.org/partners/ibm-skills-network)
