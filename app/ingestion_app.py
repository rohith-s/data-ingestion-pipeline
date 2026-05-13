
from services.database_service import save_to_database,test_connection
from services.json_writer import write_json
from services.file_processor import process_file


def run_ingestion(file_path):
    # Step 1: Read and Convert File
    json_data = process_file(file_path)
    
    # Step 2: Save JSON Output
    output_file = write_json(json_data)

    # Step 3: Save into Database
    save_to_database(json_data)

    print(f"processing completed successfully: {output_file}")