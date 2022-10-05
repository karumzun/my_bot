from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot, ADMINS
from keyboards.client_cb import cancel_markup
from database import bot_db
from database.bot_db import sql_create


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


async def fsm_start(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.answer('Не достаточно уполномоченый')
    else:
        if message.chat.type == 'private':
            await FSMAdmin.photo.set()
            await message.answer('Скиньте фотку блюда', reply_markup=cancel_markup)

        else:
            await message.answer('Пиши в личку')

async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.from_user.id
        data['username'] = f'@{message.from_user.username}'
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.answer('Напишите название блюда')

async def name_of_dish(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer('Напишите описание блюда')


async def description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.answer('Напишите цену блюда')


async def price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
        await bot.send_photo(message.from_user.id, data['photo'],
                             caption=f"Название блюда: {data['name']}\n"
                                     f"Описание: {data['description']}\n"
                                     f"Цена: {data['price']}\n\n"
                                     f"Добавил: {data['username']}")
    await bot_db.sql_command_insert(state)
    await state.finish()
    await message.answer('Cвободен')


async def cancel_registration(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()





def register_handlers_fsmAdminMenu(dp: Dispatcher):
    dp.register_message_handler(cancel_registration, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_registration,
                                Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_photo, state=FSMAdmin.photo, content_types=['photo'])
    dp.register_message_handler(name_of_dish, state=FSMAdmin.name)
    dp.register_message_handler(description, state=FSMAdmin.description)
    dp.register_message_handler(price, state=FSMAdmin.price)

