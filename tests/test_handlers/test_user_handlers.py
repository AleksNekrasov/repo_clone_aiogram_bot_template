from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram import Router, F
from aiogram.types import ReplyKeyboardRemove

from tests.test_lexicon.test_lexicon import LEXICON_RU
from tests.test_keyboards.test_keyboards import animal_keyboard

router = Router()

# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'],
                         reply_markup=animal_keyboard)

@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU.get('/help'))

@router.message(F.text == 'Собак 🦮')
async def process_dog_answer(message: Message):
    await message.answer(
        text='Да, несомненно, кошки боятся собак. '
             'Но вы видели как они боятся огурцов?',
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(F.text == 'Огурцов 🥒')
async def process_cucumber_answer(message: Message):
    await message.answer(
        text='Да, иногда кажется, что огурцов '
             'кошки боятся больше'
    )


