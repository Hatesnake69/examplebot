import os
from dotenv import load_dotenv

from aiogram.contrib.fsm_storage.redis import RedisStorage2

load_dotenv()

BOT_TOKEN: str = os.getenv("BOT_TOKEN")

FROM_EMAIL: str = os.getenv("FROM_EMAIL")
PASSWORD: str = os.getenv("PASSWORD")

REDIS_HOST: str = os.getenv('REDIS_HOST')  # это для редиса
REDIS_PORT: str = os.getenv('REDIS_PORT')  # это для редиса

WEBHOOK_HOST: str = os.getenv("WEBHOOK_HOST")
WEBHOOK_PATH: str = os.getenv("WEBHOOK_PATH")
WEBAPP_HOST: str = os.getenv("WEBAPP_HOST")
WEBAPP_PORT: str = os.getenv("WEBAPP_PORT")
CREDENTIALS_PATH: str = os.getenv("CREDENTIALS_PATH") #BigQuery
PROJECT: str = os.getenv("PROJECT") #BigQuery

cache = RedisStorage2(host=REDIS_HOST, port=int(REDIS_PORT))
webhook_url = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'
