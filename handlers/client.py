from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp


async def start(message: types.Message):
    await message.answer(f'Привет {message.from_user.first_name}')



async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('NEXT', callback_data='button_call_1')
    markup.add(button_call_1)

    question = 'Корень из 49%'
    answers = ['7', '0,7', '70', '0,07']

    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=10,
        reply_markup=markup


    )


async def mem(message: types.message):
    photo = open('media/it-юмор-geek-doge-Мемы-5952251.png', 'rb')
    await bot.send_photo(message.from_user.id, photo)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(mem, commands=['mem'])