import sqlite3
from aiogram import types, Dispatcher
from config import bot

def sql_create():
    global db, cursor
    db = sqlite3.connect('bot.sqlite3')
    cursor = db.cursor()
    if db:
        print('fas')

    db.execute('CREATE TABLE IF NOT EXISTS menu'
               '(id INTEGER PRIMARY KEY, username TEXT, '
               'photo TEXT, name TEXT, description TEXT, '
               'price INTEGER)')
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute('INSERT INTO menu VALUES (?, ?, ?, ?, ?, ?)', tuple(data.values()))
        db.commit()
async def list_menu(message):
    l1st = cursor.execute('SELECT * FROM menu').fetchall()
    for i in l1st:
        await message.answer(f'Название блюда: {i[3]} Описание: {i[4]}')


async def full_description(message):
    l1st = cursor.execute('SELECT * FROM menu').fetchall()
    for i in l1st:
        await bot.send_photo(message.from_user.id, i[2],
                             caption=f"Название блюда: {i[3]}\n"
                                     f"Описание: {i[4]}\n"
                                     f"Цена: {i[5]}\n\n"
                                     f"Добавил: {i[1]}")


