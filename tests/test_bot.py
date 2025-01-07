import  asyncio
import os
import logging

from  aiogram import Bot, Dispatcher
from test_config.test_config_data import TestConfig, test_load_config
from test_handlers import test_outer_handlers, test_user_handlers

# Инициализируем логгер
logger = logging.getLogger(__name__)

async def main():
    # Определяем абсолютный путь к каталогу проекта--------------------------
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Указываем путь к файлу .env
    env_file_path = os.path.join(project_root, 'config', '.env')
    #------------------------------------------------------------------------

    # Конфигурируем логирование
    logging.basicConfig(level=logging.INFO,
                        format='%(filename)s:%(lineno)d #%(levelname)-8s '
                                '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    config: TestConfig = test_load_config(env_file_path)

    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    #  Регистриуем роутеры в диспетчере
    dp.include_router(test_user_handlers.router)
    dp.include_router(test_outer_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

