from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Database Configuration
MYSQL_CONNECTION_STRING = os.getenv("MYSQL_CONNECTION_STRING")

# Output JSON Folder
OUTPUT_JSON_PATH = os.getenv("OUTPUT_JSON_PATH")

# Log Folder
LOG_PATH = os.getenv("LOG_PATH")