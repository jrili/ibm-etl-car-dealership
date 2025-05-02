import os
import pandas as pd

from . import config
from . import logging_utils

def load(target_file, transformed_df: pd.DataFrame):
    logging_utils.log(f"In load_data(): Loading data to file '{target_file}'")
    transformed_df.to_csv(target_file, index=False)
    logging_utils.log(f"In load_data(): Done loading data to file '{target_file}'")

def validate_load(output_file, transformed_df):
    logging_utils.log("In validate_load(): started")

    assert (os.path.exists(output_file)), f"validate_load(): Output file '{output_file}' not found "

    df_from_output_file = pd.read_csv(output_file)

    # Assert expected number of columns
    assert (df_from_output_file.shape[1] == len(config.COLUMN_NAMES)), f"validate_load():Required number of columns is '{len(config.COLUMN_NAMES)}' but found '{df_from_output_file.shape[1]}'"

    # Assert expected columns exist in result
    for column in config.COLUMN_NAMES:
        assert (column in df_from_output_file.columns), f"validate_load(): Required column '{column}' not found in extracted dataframe"

    assert (df_from_output_file.equals(transformed_df)), f"validate_load(): Missing/mismatched data detected in output file '{output_file}' "

    logging_utils.log("In validate_load(): ended")
