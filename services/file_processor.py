import os
import pandas as pd
import json
import logging
logger = logging.getLogger(__name__)

SUPPORTED_EXTENSIONS = [".xlsx", ".xls", ".csv", ".json"]


def process_file(file_path):
    """
    Main orchestration function for file processing.

    Steps:
    1. Resolve file path
    2. Validate file
    3. Detect file type
    4. Read file
    5. Convert to JSON structure
    6. Return JSON variable
    """
    try:
        logger.info(f"File Processing started for file: {file_path}")

        # Resolve file path
        resolved_file_path = _resolve_file_path(file_path)
        logger.info(f"Resolved file path: {resolved_file_path}")

        # validate file path
        _validate_file_path(resolved_file_path)

        # Detect file type / Extension
        _, extension = os.path.splitext(resolved_file_path)
        extension = extension.lower()
        logger.info(f"Detected file extension: {extension}")

        if extension in [".xlsx", ".xls"]:
            logger.info("Processing Excel File")
            json_data = _read_excel_file(resolved_file_path)
        elif extension in [".csv"]:
            logger.info("Processing CSV File")
            json_data = _read_csv_file(resolved_file_path)

        elif extension in [".json"]:
            logger.info("Processing JSON File")
            json_data = _read_json_file(resolved_file_path)

        else:
            logger.info("Unsupported File Format")
            raise ValueError(f"Unsupported file type: {extension}")

        logger.info(f"Total records processed: {len(json_data)}")
        logger.info("File processing completed successfully")

        return json_data

    except Exception as ex:
        logger.error(f"Error while processing file: {str(ex)}")
        raise


def _resolve_file_path(file_path):
    """
    Resolve relative and absolute file paths.
    """
    try:
        logger.info("Resolving file path")
        # Absolute path
        if os.path.isabs(file_path):
            logger.info("Absolute path detected")
            return file_path

        # Relative path
        logger.info("Relative path detected")
        _project_root = os.getcwd()
        _resolved_path = os.path.join(_project_root, file_path)
        return os.path.abspath(_resolved_path)

    except Exception as ex:
        logger.error(f"Error while resolving file path: {str(ex)}")
        raise


def _validate_file_path(file_path):
    """
    Validate:
    - File exists
    - Supported extension
    """
    try:
        logger.info("Validating file path")
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File does not exist: {file_path}")
        _, extension = os.path.splitext(file_path)
        extension = extension.lower()
        if extension not in SUPPORTED_EXTENSIONS:
            raise ValueError(f"Unsupported file extension: {extension}")
        logger.info("File path validation successful")
    except Exception as ex:
        logger.error(f"File validation failed: {str(ex)}")
        raise


def _read_excel_file(file_path):
    """
    Read Excel file.
    Only first sheet will be processed.
    """
    try:
        logger.info("Reading Excel File")
        dataframe = pd.read_excel(file_path, sheet_name=0)
        logger.info(f"Excel file read successfully. Rows: {len(dataframe)}")
        return _convert_dataframe_to_json(dataframe)
    except Exception as ex:
        logger.error(f"Error reading Excel file: : {str(ex)}")
        raise


def _read_csv_file(file_path):
    """
    Read CSV file.
    """
    try:
        logger.info("Reading CSV File")
        dataframe = pd.read_csv(file_path)
        logger.info(f"CSV file read successfully. Rows: {len(dataframe)}")
        return _convert_dataframe_to_json(dataframe)
    except Exception as ex:
        logger.error(f"Error Reading CSV file: {str(ex)}")
        raise


def _read_json_file(file_path):
    """
    Read JSON file directly into memory.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as json_file:
            json_data = json.load(json_file)
        logger.info(
            f"JSON file read successfully. Records: {len(json_data)}")
        return json_data
    except Exception as ex:
        logger.error(f"Error reading JSON file: {str(ex)}")
        raise


def _convert_dataframe_to_json(dataframe):
    """
    Convert pandas dataframe into JSON structure.
    """
    try:
        # Normaalize column names
        dataframe.columns = [col.strip().lower() for col in dataframe.columns]

        # Replace NaN values with None
        dataframe = dataframe.where(pd.notnull(dataframe), None)

        _json_data = dataframe.to_dict(orient="records")
        logger.info(f"Dataframe converted to JSON successfully")

        return _json_data
    except Exception as ex:
        logger.error(f"Error converting dataframe to JSON: {str(ex)}")
        raise
