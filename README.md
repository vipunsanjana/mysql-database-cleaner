# MySQL Data Cleanup Script

## Overview
This script is designed to clean up all records from a MySQL database using Python. It also provides notifications via Google Chat for successful and failed cleanup attempts.

## Features
- Connects to a MySQL database
- Deletes all records from the database
- Logs success and failure messages
- Sends notifications to Google Chat

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- Required dependencies (listed in `requirements.txt`)
- A MySQL database
- Google Chat webhook for notifications

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/vipunsanjana/mysql-database-cleaner
   cd mysql-database-cleaner
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Configuration
Update the necessary configuration files or environment variables:
- MySQL connection details
- Google Chat webhook URL
- Logging configurations

## Usage
Run the script with the following command:
```sh
python main.py
```

## Code Structure
```
app/
│── services/
│   ├── google_chat_service/
│   │   ├── google_chat.py   # Handles Google Chat notifications
│   ├── mysql_service/
│   │   ├── connection.py    # Establishes MySQL connection
│   │   ├── dataclean.py     # Deletes records from MySQL database
│── utils/
│   ├── constants.py         # Stores constants and logging configurations
│── main.py                  # Entry point of the script
```

## Logging
Logs are maintained in `constants.LOGGER` and include:
- Successful cleanup messages
- Error messages in case of failure

## Error Handling
If an error occurs during cleanup, the script:
- Logs the error
- Sends a failure notification to Google Chat

## Contact
For any issues or questions, contact **SOC Team - WSO2 LLC**.
**Developed by Vipun Sanjana**.
