import requests
import os
from datetime import datetime
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
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
    logger.info("Attempting to stop service...")
    query = f"""
    mutation {{
        serviceStop(id: "{SERVICE_ID}") {{
            id
        }}
    }}
    """
    response = requests.post(API_URL, json={'query': query}, headers=headers)
    logger.info(f"Stop response: {response.json()}")

def start_service():
    logger.info("Attempting to start service...")
    query = f"""
    mutation {{
        serviceStart(id: "{SERVICE_ID}") {{
            id
        }}
    }}
    """
    response = requests.post(API_URL, json={'query': query}, headers=headers)
    logger.info(f"Start response: {response.json()}")

if __name__ == "__main__":
    logger.info("Script started")
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logger.info(f"Current time: {current_time}")
    action = os.getenv("ACTION")
    logger.info(f"Action: {action}")
    if action == "start":
        start_service()
    elif action == "stop":
        stop_service()
    else:
        logger.warning("No valid action provided")



from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/logs")
async def get_logs():
    with open("/app/cron.log", "r") as file:
        logs = file.read()
    return PlainTextResponse(logs)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)