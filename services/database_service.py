
import logging

from config import MYSQL_CONNECTION_STRING
from sqlalchemy import create_engine,text

logger = logging.getLogger(__name__)

def save_to_database(json_data):
    pass

def test_connection():
    try:
        logger.info("Testing MySQL Database Connection")
        engine = create_engine(MYSQL_CONNECTION_STRING)
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            logger.info(result.fetchone())
            logger.info("MySQL Database Connection Successful")
    except Exception as e:
        logger.error(e)
        logger.error(f"MySQL Database Connection Failed: {str(e)}")  