from app.utils import config, constants
import requests
from app.utils.constants import VALID_CONTENT_TYPE

def send_message_to_webhook(message: str) -> dict:
    """
    Send a message to the configured webhook URL.

    Args:
        message (str): The message to send.

    Returns:
        dict: A dictionary containing the message.
    """
    try:
        webhook_url = config.WEB_HOOK_URL
        headers = {"Content-Type": VALID_CONTENT_TYPE}
        payload_text = {"text": message}

        response = requests.post(webhook_url, json=payload_text, headers=headers)

        if response.status_code == 200:
            constants.LOGGER.info("Message sent successfully.")
            return {"message": "Message sent successfully."}
        else:
            constants.LOGGER.error(f"Failed to send message, status code: {response.status_code}")
            raise Exception(f"Failed to send message, status code: {response.status_code}")

    except Exception as e:
        constants.LOGGER.error(f"Failed to send message: {e}")
        raise Exception(f"Failed to send message: {e}")

def notify_successful_mysql_cleanup() -> dict:
    """VALID_CONTENT_TYPES
    Send a success notification for MySQL table cleanup.

    Returns:
        dict: A dictionary containing the success message.
    """
    message = "✅ Successfully cleaned the MySQL 'phishing_metadata' table."
    return send_message_to_webhook(message)

def notify_failed_mysql_cleanup(e: Exception) -> dict:
    """
    Send a failure notification for MySQL table cleanup.

    Args:
        e (Exception): The exception that occurred during cleanup.

    Returns:
        dict: A dictionary containing the failure message.
    """
    message = f"❌ Failed to clean the MySQL 'phishing_metadata' table: {str(e)}"
    return send_message_to_webhook(message)