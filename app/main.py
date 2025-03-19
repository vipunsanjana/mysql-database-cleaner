from app.services.google_chat_service.google_chat import notify_failed_mysql_cleanup, notify_successful_mysql_cleanup
from app.services.mysql_service.connection import create_mysql_connection
from app.services.mysql_service.dataclean import delete_all_records
from app.utils import constants

def main():
    """
    Main function to clean Firebase Storage
    """
    try:
        #Delete all records from the MySQL database
        connection = create_mysql_connection()
        delete_all_records(connection)
        notify_successful_mysql_cleanup()
    except Exception as e:
        notify_failed_mysql_cleanup(e)
        constants.LOGGER.error(constants.MSG_MYSQL_CLEANUP_FAILED.format(e))

if __name__ == "__main__":
    main()