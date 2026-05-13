import logger_config

from app.ingestion_app import run_ingestion
from services.database_service import test_connection

if __name__ == "__main__":
    logger_config.logger.info("Starting Data Ingestion Application")
    test_connection()
    file_path= input("Enter the file path: ")
    run_ingestion(file_path)