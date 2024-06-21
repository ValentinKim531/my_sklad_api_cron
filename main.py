import os
from datetime import datetime
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, filename='/app/cron.log', filemode='a', format='%(asctime)s - %(message)s')

if __name__ == "__main__":
    logging.info("Script started")
    action = os.getenv("ACTION")
    logging.info(f"Script started with action: {action}")

    if action == "start":
        logging.info("Performing start action")
        # Ваша логика для start
    elif action == "stop":
        logging.info("Performing stop action")
        # Ваша логика для stop
    else:
        logging.info("No valid action provided")
