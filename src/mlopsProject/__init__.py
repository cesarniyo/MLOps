import os
import sys
import logging

# defining the log format
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]" 

# create a folder to host the logs
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
log_filepath = os.path.join(log_dir,"running_logs.log")


# define logging basic configuration
logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath), # print logs into a file
        logging.StreamHandler(sys.stdout)  # print logs into a terminal
    ]
)

logger = logging.getLogger("mlopsProjectLogger") # create the logging object

#=======================================================
# To test the logging go to main.py and then do this as an example:
"""
from mlopsProject import logger

STAGE_NAME = "Data Ingestion stage"
logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 

"""