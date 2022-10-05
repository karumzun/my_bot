import random

from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp
from database.bot_db import list_menu
from handlers.parse import parser


async def menu(message: types.Message):
    await message.answer('Для получения полной информации о блюде, Напишите название блюда в точности как оно записанно в меню')
    await list_menu(message)





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

async def parser_news(message: types.Message):
    items = parser()
    for item in items:
        await bot.send_message(
            message.from_user.id,
            text=f"{item['link']}\n\n"
                 f"{item['title']}\n\n"
                 f"{item['time']}, "
                 f"#Y{item['day']}, "
                 f"#{item['year']}\n"
        )
async def mem(message: types.message):
    photoes = ['media/it-юмор-geek-doge-Мемы-5952251.png', 'media/photo_5285336714249880692_y.jpg',
             'media/photo_5285336714249880693_y.jpg', 'media/photo_5328085795057287694_x.jpg']
    random_photo = random.choice(photoes)
    photo = open(random_photo, 'rb')
    await bot.send_photo(message.from_user.id, photo)


def register_handlers_client(dp: Dispatcher):

    dp.register_message_handler(menu, commands=['menu'])

    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(mem, commands=['mem'])
    dp.register_message_handler(parser_news, commands=['news'])