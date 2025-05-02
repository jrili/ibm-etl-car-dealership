from datetime import datetime 

from . import config

def log(msg, tee_enabled=True):
    """Logs a message to the configured log file path

    Keyword Arguments:
    - msg -- string message to log
    - tee_enabled -- set to True to mirror log prints to stdout 
        - Default: True
    
    Return Values:
    - None
    """
    timestamp_format = "%Y-%m-%d-%H:%M:%S"
    now = datetime.now()
    timestamp_str = now.strftime(timestamp_format)

    with open(config.LOG_FILE_PATH, "a") as f:
        log_str = timestamp_str + "," + msg
        if tee_enabled:
            print(log_str)
        f.write(log_str + "\n")
