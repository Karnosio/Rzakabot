import logging
from aiogram import executor

from handlers import dp

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info("Starting bot..")
    try:
        executor.start_polling(dp, skip_updates=True)
    except (KeyboardInterrupt, SystemExit):
        logger.warning("Bot was stopped")
