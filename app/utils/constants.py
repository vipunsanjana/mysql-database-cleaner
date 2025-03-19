import logging
from app.utils import config

# Configure logging
logging.basicConfig(
    level=getattr(logging, config.LOGGING_LEVEL, logging.INFO),
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)

# Create a logger
LOGGER = logging.getLogger(__name__)

# Success Messages
MSG_MYSQL_CLEANUP_SUCCESS = "Successfully cleaned the MySQL 'phishing_metadata' table."
MSG_MYSQL_NO_ROWS_IN_TABLE = "No records were deleted from phishing_metadata."
MSG_MYSQL_ROWS_IN_TABLE = "{} records were deleted from phishing_metadata."

# Error Messages
MSG_MYSQL_CLEANUP_FAILED = "Failed to clean the MySQL 'phishing_metadata' table: {}"

# web page content types
VALID_CONTENT_TYPE = "application/json"
