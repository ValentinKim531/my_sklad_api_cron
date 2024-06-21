import requests
import os
from datetime import datetime
import logging
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import uvicorn

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


app = FastAPI()


@app.get("/logs")
async def get_logs():
    logger.info("Fetching logs")
    try:
        with open("/app/cron.log", "r") as file:
            logs = file.read()
        return PlainTextResponse(logs)
    except Exception as e:
        logger.error(f"Error fetching logs: {e}")
        return PlainTextResponse("Error fetching logs")


if __name__ == "__main__":
    action = os.getenv("ACTION")
    logger.info(f"{datetime.now()} - Script started with action: {action}")
    if action == "start":
        start_service()
    elif action == "stop":
        stop_service()
    else:
        logger.error(f"{datetime.now()} - No valid ACTION provided")

    logger.info("Starting FastAPI application")
    uvicorn.run(app, host="0.0.0.0", port=8000)
