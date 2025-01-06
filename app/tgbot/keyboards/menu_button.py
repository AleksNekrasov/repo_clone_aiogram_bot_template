import logging

from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault
#from fluentogram import TranslatorRunner

logger = logging.getLogger(__name__)

async def set_main_menu(bot: Bot):
    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [
        BotCommand(command='/help',
                   description='Справка по работе бота'),
        BotCommand(command='/support',
                   description='Поддержка'),
        BotCommand(command='/contacts',
                   description='Другие способы связи'),
        BotCommand(command='/payments',
                   description='Платежи')
    ]

    await bot.set_my_commands(main_menu_commands)


# async def set_main_menu_button(bot: Bot, i18n: TranslatorRunner):
#     menu_commands = {
#         '/lang': i18n.lang.command.description(),
#         '/help': i18n.help.command.description()
#     }
#     main_menu_commands = [
#         BotCommand(
#             command=command,
#             description=description
#         ) for command, description in menu_commands.items()
#     ]
#     await bot.set_my_commands(main_menu_commands, scope=BotCommandScopeDefault())