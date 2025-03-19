import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv(override=True)

# Google Chat Configuration
WEB_HOOK_URL = os.getenv("WEB_HOOK_URL")

# Mysql Database Configuration
MYSQL_DB_HOST = os.getenv("MYSQL_DB_HOST")
MYSQL_DB_USER = os.getenv("MYSQL_DB_USER")
MYSQL_DB_PASSWORD = os.getenv("MYSQL_DB_PASSWORD")
MYSQL_DB_NAME = os.getenv("MYSQL_DB_NAME")
MYSQL_DB_PORT = os.getenv("MYSQL_DB_PORT")

# Logger level
LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "INFO").upper()

# List of all required environment variables
required_vars = [
    "WEB_HOOK_URL",
    "MYSQL_DB_HOST",
    "MYSQL_DB_USER",
    "MYSQL_DB_PASSWORD",
    "MYSQL_DB_NAME",
    "MYSQL_DB_PORT",
]

# Check for missing environment variables
missing_vars = [var_name for var_name in required_vars if not os.getenv(var_name)]

if missing_vars:
    raise ValueError(
        f"Missing required environment variables: {', '.join(missing_vars)}"
    )