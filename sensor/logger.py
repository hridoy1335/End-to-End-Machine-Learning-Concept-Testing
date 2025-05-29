# importing dependency
import os
import logging
from datetime import datetime

# building the custom logger file and folder with using the current datatime
LOG_FOLDER = "logs"
CURRENT_TIME_STAMP = datetime.now().strftime("%d-%m-%Y__%H:%M:%S")

LOG_FILE = f"{CURRENT_TIME_STAMP}.log"
LOG_PATH = os.path.join(os.getcwd(),LOG_FOLDER)

os.makedirs(LOG_PATH,exist_ok=True)
LOG_FILE_PATH = os.path.join(LOG_PATH,LOG_FILE)

# defining the logging format and INFO
logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO
)