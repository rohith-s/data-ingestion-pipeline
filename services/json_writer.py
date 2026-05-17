import os
import json
import logging

from datetime import datetime

from config import OUTPUT_JSON_PATH

logger = logging.getLogger(__name__)

def print_output_json_path():
    print(OUTPUT_JSON_PATH)

def write_json(json_data, skip):
    """
    Write JSON data into output folder.

    Returns:
        output_file_path (str) if saved
        None if skipped
    """
    try:

        # skip
        if skip:
            logger.info("Skipping JSON file writing")
            return None
        
        # Create output folder if not exists
        if not os.path.exists(OUTPUT_JSON_PATH):
            os.makedirs(OUTPUT_JSON_PATH)
        
        # Generate timestamp for filename
        _timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]

        filename = f"{_timestamp}.json"
        
        output_file_path = os.path.join(OUTPUT_JSON_PATH, filename)

        logger.info(f"Writing JSON file to: {output_file_path}")

        # Write JSON
        with open(output_file_path, "w", encoding="utf-8") as json_file:
            json.dump(json_data, json_file, indent=4, default=str)
        logger.info(f"JSON output file created successfully")

        return output_file_path
    except Exception as ex:
        logger.error(f"Error while writing JSON file: {str(ex)}")
        raise