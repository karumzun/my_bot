from aiogram import types
from aiogram.utils import executor
from config import bot, dp
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f'Привет {message.from_user.first_name}')


@dp.message_handler(commands=['quiz'])
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

@dp.callback_query_handler(lambda call: call.data == 'button_call_1')
async def quiz_2(call: types.CallbackQuery):

    question = '2+2*2'
    answers = ['8', '4', '22', '6']

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=-1,
        open_period=10,


    )
@dp.message_handler(commands=['mem'])
async def mem(message: types.message):
    photo = open('media/it-юмор-geek-doge-Мемы-5952251.png', 'rb')
    await bot.send_photo(message.from_user.id, photo)


@dp.message_handler(content_types=['text', 'photo'])
async def echo(message: types.Message):
    try:
        a = int(message.text)
        await bot.send_message(message.from_user.id, a*a)

    except:



        await bot.send_message(message.from_user.id, message.text)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
