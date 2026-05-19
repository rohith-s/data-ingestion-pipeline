
import json
import logging


from sqlalchemy import create_engine, text

from config import MYSQL_CONNECTION_STRING

logger = logging.getLogger(__name__)


def save_to_database(json_data):
    """
    Save JSON records into MySQL
    using stored procedure:
    sp_upsert_user_information
    """
    try:
        logger.info("Database save operation started")
        if not json_data:
            logger.warning("No data available for database processing")
            return
        # Create engine
        engine = mysql_engine()
        total_records = len(json_data)
        logger.info(f"Total records received: {total_records}")
        successful_records = 0
        failed_records = 0
        # Begin Transaction
        with engine.begin() as connection:
            for index, record in enumerate(json_data, start=1):
                try:
                    logger.info(f"Processing database record: {index}")

                    # convert profile_json dictionary to JSON string
                    profile_json = record.get(
                        "profile_json"
                    )

                    if isinstance(profile_json, dict):
                        profile_json = json.dumps(profile_json)

                    # Execute Stored Procedure
                    connection.execute(

                        text(
                            """
                            CALL sp_upsert_user_information
                            (
                                :employee_code,
                                :first_name,
                                :last_name,
                                :email,
                                :phone_number,
                                :date_of_birth,
                                :salary,
                                :bonus_percentage,
                                :is_active,
                                :joining_datetime,
                                :last_login_timestamp,
                                :profile_json,
                                :profile_picture,
                                :rating,
                                :gender,
                                :created_by,
                                :updated_by
                            )
                            """
                        ),

                        {
                            "employee_code":
                                record.get("employee_code"),

                            "first_name":
                                record.get("first_name"),

                            "last_name":
                                record.get("last_name"),

                            "email":
                                record.get("email"),

                            "phone_number":
                                record.get("phone_number"),

                            "date_of_birth":
                                record.get("date_of_birth"),

                            "salary":
                                record.get("salary"),

                            "bonus_percentage":
                                record.get("bonus_percentage"),

                            "is_active":
                                record.get("is_active"),

                            "joining_datetime":
                                record.get("joining_datetime"),

                            "last_login_timestamp":
                                record.get(
                                    "last_login_timestamp"
                                ),

                            "profile_json":
                                profile_json,

                            "profile_picture":
                                record.get(
                                    "profile_picture"
                                ),

                            "rating":
                                record.get("rating"),

                            "gender":
                                record.get("gender"),

                            "created_by":
                                record.get("created_by"),

                            "updated_by":
                                record.get("updated_by")
                        }
                    )
                    successful_records += 1

                    logger.info(
                        f"Database record processed successfully: {index}"
                    )

                except Exception as record_exception:
                    failed_records += 1
                    logger.error(
                        f"Failed processing record {index}: "
                        f"{str(record_exception)}"
                    )
                    logger.error(
                        f"Failed record data: {record}"
                    )
                    raise
        logger.info("Database save operation completed")
        logger.info(f"Successful records: {successful_records}")

        logger.info(f"Failed records: {failed_records}")

    except Exception as ex:
        logger.error(f"Database save operation failed: {str(ex)}")
        raise


def test_connection():
    try:
        logger.info("Testing MySQL Database Connection")
        engine = mysql_engine()
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            logger.info(result.fetchone())
            logger.info("MySQL Database Connection Successful")
    except Exception as e:
        logger.error(e)
        logger.error(f"MySQL Database Connection Failed: {str(e)}")


def mysql_engine():
    """
    Create and return MySQL SQLAlchemy engine.
    """
    try:
        logger.info(
            "Creating MySQL database engine"
        )
        engine = create_engine(MYSQL_CONNECTION_STRING, pool_pre_ping=True)
        """
        Why pool_pre_ping=True?
        VERY IMPORTANT.

        This automatically:

        1. checks stale connections
        2. reconnects dead pooled connections
        3. avoids:
            3.1 MySQL server has gone away

        This is standard production practice.
        """
        logger.info("MySQL database engine created successfully")
        return engine
    except Exception as e:
        logger.error(f"MySQL database engine creation failed: {str(e)}")
        raise