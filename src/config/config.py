import os
import logging
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv()

logger = logging.getLogger("vehicles_c2s")
logger.setLevel(logging.DEBUG)
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

API_KEY = os.getenv("OPENAI_API_KEY")
