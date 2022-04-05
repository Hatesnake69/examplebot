from aiogram import Bot, types
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


from app.handlers.common import register_handlers_common

from config import (BOT_TOKEN, WEBAPP_HOST, WEBAPP_PORT, WEBHOOK_PATH, cache,
                    webhook_url)


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot, storage=RedisStorage2())

register_handlers_common(dp)


if __name__ == '__main__':
    executor.start_polling(dp)
    # print(cache.scan_iter())
    # executor.start_webhook(dispatcher=dp,
    #                        webhook_path=WEBHOOK_PATH,
    #                        on_startup=on_startup,
    #                        skip_updates=True,
    #                        host=WEBAPP_HOST,
    #                        port=WEBAPP_PORT)

