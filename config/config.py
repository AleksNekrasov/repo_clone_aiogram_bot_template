# from dynaconf import Dynaconf
#
# settings = Dynaconf(
#     envvar_prefix=False,  # "DYNACONF",
#     environments=True,  # Автоматически использовать секцию текущей среды
#     env_switcher="ENV_FOR_DYNACONF",
#     settings_files=['settings.toml', '.secrets.toml'],
#     load_dotenv=True
# )

from dataclasses import dataclass
from environs import Env

@dataclass
class DatabaseConfig:
    database: str         # Название базы данных
    db_host: str          # URL-адрес базы данных
    db_user: str          # Username пользователя базы данных
    db_password: str      # Пароль к базе данных

@dataclass
class TgBot:
    token: str            # Токен для доступа к телеграм-боту
    admin_ids: list[int]  # Список id администраторов бота

@dataclass
class Config:
    tg_bot: TgBot         # класс TgBot
    db: DatabaseConfig    # класс DatabaseConfig

def load_config(path: str | None = None) -> Config:
    # Создаем экземпляр класса Env
    env: Env = Env()

    # Добавляем в переменные окружения данные, прочитанные из файла .env
    env.read_env()

    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
            admin_ids=list(map(int, env.list('ADMIN_IDS')))
        ),
        db=DatabaseConfig(
            database=env('DATABASE'),
            db_host=env('DB_HOST'),
            db_user=env('DB_USER'),
            db_password=env('DB_PASSWORD')
        )
    )






