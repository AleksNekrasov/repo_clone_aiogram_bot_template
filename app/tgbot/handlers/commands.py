from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode
from fluentogram import TranslatorRunner

from app.services.delay_service.publisher import delay_message_deletion
from app.tgbot.states.start import StartSG
from nats.js.client import JetStreamContext

commands_router = Router()


@commands_router.message(CommandStart())
async def process_start_command(
    message: Message,
    dialog_manager: DialogManager,
    i18n: TranslatorRunner
) -> None:
    await dialog_manager.start(state=StartSG.start, mode=StartMode.RESET_STACK)


# Этот хэндлер будет срабатывать на команду /del
@commands_router.message(Command('del'))
async def send_and_del_message(
    message: Message, 
    i18n: TranslatorRunner, 
    js: JetStreamContext, 
    delay_del_subject: str
) -> None:
    
    delay = 3
    msg: Message = await message.answer(text=i18n.will.delete(delay=delay))
    
    await delay_message_deletion(
        js=js,  
        chat_id=msg.chat.id, 
        message_id=msg.message_id,
        subject=delay_del_subject, 
        delay=delay
    )


# @commands_router.message(Command('help'))
# async def process_help_command(
#     message: Message,
#     dialog_manager: DialogManager,
#     i18n: TranslatorRunner
# ) -> None:
#     await message.answer(text=i18n.help.command())
