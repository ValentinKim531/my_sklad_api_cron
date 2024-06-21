
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, filename='/app/cron.log', filemode='a', format='%(asctime)s - %(message)s')


logging.info("main.py is run")


if __name__ == "__main__":
    logging.info("Script started")

