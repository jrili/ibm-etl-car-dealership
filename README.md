ETL Project: Car Dealership Data
===================================
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) 
[ETL]

***Part of a Data Engineer Portfolio: [jrili/data-engineer-portfolio](https://github.com/jrili/data-engineer-portfolio)***

# Project Description
This project is an Extract, Transform, Load (ETL) pipeline designed for a car dealership's data processing. It involves collecting and transforming data from different sources to prepare it for analysis and future integration into a database.

# Project Objectives
* Extract car dealership data from multiple sources
* Cleanse, combine, and format data for consistency
* Structure data for future use in analytics or database systems

# Tools & Technologies Used
* Python 3.13
* Pandas
* Jupyter Notebook

# Specifications
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

# Workflow Overview
* Fetch data from source files (CSV, JSON, XML)
* Combine and transform the data using Python and Pandas
* Output the transformed data for inspection or future loading steps.

# How to Execute Script:
## Prerequisites
### 1.  Gather the data files
```
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/datasource.zip
```

> [!NOTE]
> In case of unavailability, a snapshot of datasource.zip is also available in the root directory.
> Date of snapshot: `2025 Mar 24`

### 2. Unzip the downloaded file into a directory named `datasource`
```
unzip source.zip -d datasource
```

### 3. Install required libraries
```
python -m pip install -r requirements.txt
```

## Execution Steps
_(Tested in Python 3.13)_
```
python etl_practice.py
```
_Also available with sample outputs and explanations in notebook: [etl_car_dealership.ipynb](https://github.com/jrili/ibm-etl-car-dealership/blob/master/etl_car_dealership.ipynb)_
# Key Learning Points
* Building a basic ETL workflow using Python
* Data transformation and cleaning using Pandas
* Structuring data workflows for scalability

# Future Improvements
* Implement a data loading step to store transformed data in a relational database, e.g. PostgreSQL
* Add automated scheduling using tools like Apache Airflow
* Integrate validation and logging mechanisms for data quality and pipeline monitoring

# Acknowledgements
## Source Course
* [IBM: Python Project for Data Engineering (Coursera)](https://www.coursera.org/learn/python-project-for-data-engineering)
* Course Instructors:
    * Ramesh Sannareddy
    * Joseph Santarcangelo
    * Abhishek Gagneja
