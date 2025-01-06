from dataclasses import dataclass
from environs import Env
import os


@dataclass
class TestTgBot:
    token: str

@dataclass
class TestConfig:
    tg_bot: TestTgBot

def test_load_config(path: str | None = None) -> TestConfig:

    env = Env()
    env.read_env(path)

    return TestConfig(
        tg_bot=TestTgBot(
            token=env('BOT_TOKEN'))
    )