import  asyncio
import os

from  aiogram import Bot, Dispatcher
from test_config.test_config_data import TestConfig, test_load_config

async def main():
    # Определяем абсолютный путь к каталогу проекта--------------------------
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Указываем путь к файлу .env
    env_file_path = os.path.join(project_root, 'config', '.env')
    #------------------------------------------------------------------------

    config: TestConfig = test_load_config(env_file_path)

    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

