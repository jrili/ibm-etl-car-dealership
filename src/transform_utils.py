import pandas.api.types as ptypes

from . import config
from . import logging_utils

def transform(extracted_df):
    logging_utils.log("In transform(): started")
    
    # Round Price values to 2 decimal places
    extracted_df["price"] = round(extracted_df["price"], 2)

    logging_utils.log("In transform(): ended")
    return extracted_df

def validate_transform(test_df):
    logging_utils.log("In validate_transform(): started")

    # Assert expected number of columns
    assert (test_df.shape[1] == len(config.COLUMN_NAMES)), f"validate_transform():Required number of columns is '{len(config.COLUMN_NAMES)}' but found '{test_df.shape[1]}'"

    # Assert expected columns exist in result
    for column in config.COLUMN_NAMES:
        assert (column in test_df.columns), f"validate_transform(): Required column '{column}' not found in extracted dataframe"

    # Assert column data types
    assert (ptypes.is_string_dtype(test_df['car_model'])), f"validate_transform(): Expected type of column 'car_model' is 'string' but got {test_df['car_model'].dtype} "
    assert (ptypes.is_integer_dtype(test_df['year_of_manufacture'])), f"validate_transform(): Expected type of column 'year_of_manufacture' is 'integer' but got {test_df['year_of_manufacture'].dtype} "
    assert (ptypes.is_float_dtype(test_df['price'])), f"validate_transform(): Expected type of column 'price' is 'float' but got {test_df['price'].dtype} "
    assert (ptypes.is_string_dtype(test_df['fuel'])), f"validate_transform(): Expected type of column 'fuel' is 'string' but got {test_df['fuel'].dtype} "

    logging_utils.log("In validate_transform(): ended")


