import requests
import os
from datetime import datetime
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

API_URL = "https://backboard.railway.app/graphql"
API_KEY = os.getenv("RAILWAY_API_KEY")
PROJECT_ID = os.getenv("PROJECT_ID")
SERVICE_ID = os.getenv("SERVICE_ID")

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

def stop_service():
    logger.info(f"{datetime.now()} - Attempting to stop service")
    query = f"""
    mutation {{
        serviceStop(id: "{SERVICE_ID}") {{
            id
        }}
    }}
    """
    response = requests.post(API_URL, json={'query': query}, headers=headers)
    logger.info(f"{datetime.now()} - Stop response: {response.json()}")

def start_service():
    logger.info(f"{datetime.now()} - Attempting to start service")
    query = f"""
    mutation {{
        serviceStart(id: "{SERVICE_ID}") {{
            id
        }}
    }}
    """
    response = requests.post(API_URL, json={'query': query}, headers=headers)
    logger.info(f"{datetime.now()} - Start response: {response.json()}")

if __name__ == "__main__":
    logging.info("Script started")
