from mysql.connector import Error
from typing import Optional, List
from app.services.mysql_service.connection import create_mysql_connection
from app.utils import constants

def execute_query(connection, query: str, values: Optional[tuple] = None, fetch: bool = False) -> Optional[List[tuple]]:
    """
    Execute a SQL query with optional values and fetch result if required.

    Args:
        connection (mysql.connector.connection.MySQLConnection): Database connection object.
        query (str): SQL query string.
        values (tuple, optional): Values to be inserted into the query.
        fetch (bool, optional): Whether to fetch results. Defaults to False.

    Returns:
        List[tuple] or int: List of results if fetch is True, else the number of affected rows.
    Raises:
        Error: If there is an error executing the query.
    """
    try:
        with connection.cursor() as cursor:
            # Only pass `values` if it is not None or empty
            if values is not None and len(values) > 0:
                cursor.execute(query, tuple(values))
            else:
                cursor.execute(query)
            
            if fetch:
                return cursor.fetchall()
            
            connection.commit()
            return cursor.rowcount  # Return number of affected rows
    except Error as e:
        connection.rollback()
        constants.LOGGER.error(f"Database query error: {e}")
        raise Exception(f"Database query error: {e}")

def delete_all_records(connection):
    """
    Delete all records from the `phishing_metadata` table.
    Logs a message if no records are deleted.
    """
    DELETE_ALL_ANALYSES = "DELETE FROM phishing_metadata"
    result = execute_query(connection, DELETE_ALL_ANALYSES)
    
    # Check if no rows were affected
    if result == 0:
        constants.LOGGER.info(constants.MSG_MYSQL_NO_ROWS_IN_TABLE)
    else:
        constants.LOGGER.info(constants.MSG_MYSQL_ROWS_IN_TABLE.format(result))
