from . import logging_utils

def transform(data):
    logging_utils.log("In transform(): started")
    
    # Round Price values to 2 decimal places
    data["price"] = round(data["price"], 2)

    logging_utils.log("In transform(): ended")
    return data
