import os
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, filename='/app/cron.log', filemode='a', format='%(asctime)s - %(message)s')

if __name__ == "__main__":
    logging.info("Script started")
    action = os.getenv("ACTION", "No action provided")
    logging.info(f"Script started with action: {action}")
    print("Script executed")
