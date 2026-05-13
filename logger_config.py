import logging
import os


from config import LOG_PATH
from logging.handlers import TimedRotatingFileHandler

# Create logs directory if not exists
os.makedirs(LOG_PATH, exist_ok=True)

# Log file path
log_file = os.path.join(LOG_PATH,"application.log")

# Create logger
logger = logging.getLogger("DataIngestion")

logger.setLevel(logging.INFO)

# Prevent duplicate handlers
if not logger.hasHandlers():

    # Timed Rotating File Handler
    file_handler = TimedRotatingFileHandler(
        filename=log_file,
        when="midnight",
        interval=1,
        backupCount=7,
        encoding="utf-8"
    )

    # Rename rotated file suffix
    file_handler.suffix = "%Y-%m-%d"

    # Log format
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(filename)s | %(funcName)s | Line:%(lineno)d | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    file_handler.setFormatter(formatter)

    # Console Logging
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    # Root logger Configurtion
    logging.basicConfig(
        level=logging.INFO,
        handlers=[file_handler, console_handler]
    )

