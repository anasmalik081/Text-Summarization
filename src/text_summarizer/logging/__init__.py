import os, sys
import logging
from datetime import datetime

LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(os.getcwd(), 'log', LOG_FILE_NAME)
os.makedirs(LOG_FILE_PATH, exist_ok=True)

LOG_FILE = os.path.join(LOG_FILE_PATH, LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)