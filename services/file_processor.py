from logger_config import logger

def process_file(file_path):
    if file_path.endswith(".xlsx") or file_path.endswith(".xls"):
        logger.info("Processing Excel File")
    elif file_path.endswith(".csv"):
        logger.info("Processing CSV File")
    elif file_path.endswith(".json"):
        logger.info("Processing JSON File")
    else:
        logger.info("Unsupported File Format")