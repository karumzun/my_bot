import random

from aiogram import types, Dispatcher
from config import bot, dp, ADMINS
from database.bot_db import full_description


async def game(message: types.Message):
    game_list = ['⚽', '🏀', '🎾', '🎲', '🎳', '🎯']
    random_emoji = random.choice(game_list)
    if message.from_user.id not in ADMINS:
        await message.reply('Биба')

    else:
        if message.text.startswith('game'):

                await bot.send_dice(message.chat.id, emoji=random_emoji)
        else:

            await full_description(message)




async def echo(message: types.Message):
    username = f'@{message.from_user.username}' \
    if message.from_user.username is not None else message. from_user.full_name
    bad_words = ['пон', 'эчикипибарум', 'таджикистан']
    for i in bad_words:
        if i in message.text.lower():
            await bot.send_message(message.chat.id, f'рот будешь у стоматолога открывать {username}')
    try:
        a = int(message.text)
        await bot.send_message(message.from_user.id, a*a)

    except:



        await bot.send_message(message.from_user.id, message.text)





def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(game, content_types=['text'])
    dp.register_message_handler(echo, content_types=['text', 'photo'])
