import os
from loguru import logger

os.makedirs("logs", exist_ok=True)
logger.add("logs/tests.log", rotation="5 MB", level="INFO", format="{time} | {level} | {message}")

def log_step(message: str):
    logger.info(f"ШАГ: {message}")
